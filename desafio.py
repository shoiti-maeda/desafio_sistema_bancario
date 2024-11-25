import textwrap
from abc import ABC, abstractmethod
from datetime import datetime
import functools


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >=10:
            print("\n *** Você excedeu o número de transações permitidas para hoje ! ***")
            return
        
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            #print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor <= 0 or valor =="":
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
           #self._saldo += valor
            #print("\n=== Depósito realizado com sucesso! ===")
        else:
            self._saldo += valor
            #print("\n=== Depósito realizado com sucesso! ===")
            

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo: \tR$ {self.saldo}
        """

class ContaIterador:
    def __init__(self, contas:list) -> None:
        self.contas=contas
        self.contador=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            return conta 
        except IndexError:
            raise StopIteration
    

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def obter_transacoes(self, tipo=None):
        for transacao in self._transacoes:
            if tipo is None or transacao["tipo"] == tipo.__name__:
                yield transacao
                
    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao= datetime.strptime(transacao["data"],"%d-%m-%Y %H:%M:%S").date()
            if data_atual== data_transacao:
                transacoes.append(transacao)
        return transacoes

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def validar_valor(valor):
    if valor=="":
        print("Valor inválido")
        return 0
    valor=float(valor)
    return(valor)

def log_transacao(func):
    @functools.wraps(func)
    def envelope(*args,**kwargs):
        func(*args, **kwargs)
        def nome_operacao(nome_func):
            match nome_func:
                case "criar_conta":
                    return "Criação de nova conta concluído"
                case "criar_cliente":
                    return "Criação de novo cliente concluído"
                case "exibir_extrato":
                    return "Extrato "
                case "sacar":
                    return "Saque "
                case "depositar":
                    return "Depósito "
        print("\n")
        print("=" *60)
        print(f"{nome_operacao(func.__name__)} em: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}")
        print("=" *60)   
    return envelope
    

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def menu_extrato():
    menu = """\n
    ================ OPÇÕES DE EXTRATO ================
    [d]\tDepositos
    [s]\tSaques
    [t]\tTodas movimentações
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def operacao(clientes,opcao):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    
    if opcao == "d":
      depositar(cliente)  
        
    elif opcao =="s":
        sacar(cliente)
        
@log_transacao 
def depositar(cliente):
    #valor = input("Informe o valor do depósito: ")
    
    valor=(validar_valor(input("Informe o valor do depósito: ")))
    
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(cliente):
    valor=(validar_valor(input("Informe o valor do saque: ")))
    #valor = input("Informe o valor do saque: ")
    
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    transacoes = conta.historico.transacoes
    obter_transacoes = conta.historico.obter_transacoes
    cabecalho="\n================ EXTRATO ================"
    if not transacoes:
        print(cabecalho)
        print("Não foram realizadas movimentações.")
    else:
        while True:
            opcao=menu_extrato()
            match opcao:
                case "d":
                    print(cabecalho)
                    print("\nApenas depósitos:") 
                    for transacao in obter_transacoes(tipo=Deposito):
                        print(f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f} \t{transacao['data']}")
                case "s":
                    print(cabecalho)
                    print("\nApenas saques:") 
                    for transacao in obter_transacoes(tipo=Saque): 
                        print(f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f} \t{transacao['data']}")
                case "t":
                    print(cabecalho)
                    print("Todas as transações:") 
                    for transacao in obter_transacoes(): 
                        print(f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f} \t{transacao['data']}")
                case "q":
                    break
                case _:
                    print("\n@@@ Operação inválida, por favor selecione novamente   a operação desejada. @@@")

    
            print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    #print("==========================================")

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    #print("\n=== Cliente criado com sucesso! ===")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    #print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    #for conta in contas:
    #    print("=" * 100)
    #    print(textwrap.dedent(str(conta)))
    for conta in ContaIterador(contas):
        print("=" * 70)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []
    
    clientes.append(PessoaFisica(nome="Shoiti", data_nascimento="0000", cpf="0",    endereco="0000"))
    numero_conta = len(contas) + 1
    criar_conta(numero_conta, clientes, contas)
    operacao(clientes, "d")
    operacao(clientes, "s")
    

    while True:
        opcao = menu()
        match opcao:

            case "d":
                operacao(clientes, opcao)
            case "s":
                operacao(clientes, opcao)

            case "e":
                exibir_extrato(clientes)

            case "nu":
                criar_cliente(clientes)

            case "nc":
                numero_conta = len(contas) + 1
                criar_conta(numero_conta, clientes, contas)

            case "lc":
                listar_contas(contas)

            case "q":
                break

            case _:
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

    
    
main()
