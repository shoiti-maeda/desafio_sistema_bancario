from abc import ABC, abstractmethod
 

menu_principal="""  
[c] Menu Cliente 
[o] Menu Operações
[q] sair
==> """

menu_conta="""  
[d] Depositar 
[s] Sacar
[e] Extrato
[l] Listar Contas
[q] Voltar
==> """
menu_usuario="""  
[n] Novo Cliente 
[c] Nova Conta
[l] Listar Clientes
[q] Voltar
==> """

saldo = 0.0
limite = 500.0
#extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3
saques_restantes = LIMITE_SAQUES
clientes=[]
contas=[]
AGENCIA="001"
numero_conta=1



class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.sacar(self.valor)

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        
    
    def obter_saldo(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero, agencia):
        return cls(0.0, numero, agencia, cliente)
    
    
    def sacar(self, valor):
        if valor <= 0 or valor >500.0 or self.numero_saques == LIMITE_SAQUES:
            return False 
        elif self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            self.numero_saques +=1
            return True
        
     
    def depositar(self, valor):
        if valor <=0:
            return False
        else:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite, numero_saques):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite
        self.numero_saques = numero_saques
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
        
    
        
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    def __str__(self): 
        return f"PessoaFisica(nome={self.nome}, cpf={self.cpf}, endereco={self.endereco}, data_nascimento={self.data_nascimento})"

# Exemplo de uso:

# Criando um cliente Pessoa Física
#cliente = PessoaFisica(endereco=[f"{"Rua Dona Cecilia Santana"},{"70"} - {"Vila Granada"} - {"São Paulo"}/{"SP"}"], #cpf="123.456.789-00", nome="Shoiti Maeda", data_nascimento=date(1977, 10, 15))

# Criando uma Conta Corrente para o cliente
#conta = ContaCorrente(saldo=0.0, numero="001-1", agencia="0001", cliente=cliente, limite=500.0, limite_saques=3)
#conta2 = ContaCorrente(saldo=0.0, numero="002-x", agencia="0001", cliente=cliente, limite=500.0, limite_saques=3)

# Adicionando a conta ao cliente
#cliente.adicionar_conta(conta)
#cliente.adicionar_conta(conta2)


# Realizando um depósito

#if cliente.realizar_transacao(conta, Deposito(10000.0)):
#    print("Depósito efetuado.")
#else:
#    print("Operação inválida. Tente novamente.")
#    
#    
#if cliente.realizar_transacao(conta2, Deposito(10000.0)):
#    print("Depósito efetuado.")
#else:
#    print("Operação inválida. Tente novamente.")
#    
#
## Realizando um saque
#if cliente.realizar_transacao(conta, Saque(500.0)):
#    print("Saque efetuado.")
#else:
#    print("Operação inválida. Tente novamente.")
#    
#if cliente.realizar_transacao(conta, Saque(500.0)):
#    print("Saque efetuado.")
#else:
#    print("Operação inválida. Tente novamente.")
#    
#if cliente.realizar_transacao(conta, Saque(500.0)):
#    print("Saque efetuado.")
#else:
#    print("Operação inválida. Tente novamente.")
#    
#if cliente.realizar_transacao(conta2, Saque(500.0)):
#    print("Saque efetuado.")
#else:
#    print("Operação inválida. Tente novamente.")
#
## Verificando o saldo
#print(f"Saldo: {conta.obter_saldo()}")
#
## Exibindo o histórico de transações
#print(f"Número da conta: {conta.numero}, Agência: {conta.agencia}, Saldo: {conta.obter_saldo()}")
#for transacao in conta.historico.transacoes:
#    
#    print(f"Transação: {type(transacao).__name__} de {transacao.valor}")
#    
#print(f"Número da conta: {conta2.numero}, Agência: {conta2.agencia}, Saldo: {conta2.obter_saldo()}")    
#for transacao in conta2.historico.transacoes:
#    
#    print(f"Transação: {type(transacao).__name__} de {transacao.valor}")
#    
#
#for conta in cliente.contas: 
#    print(f"Número da conta: {conta.numero}, Agência: {conta.agencia}, Saldo: {conta.obter_saldo()}")
    
    
#------------------------------------------------------------------------------------------------------
#                   """ ATUALIZANDO CÓDIGO DAQUI PRA BAIXO """
#------------------------------------------------------------------------------------------------------




#def funcao_deposito(valor_deposito,saldo,/):
#        
#    if valor_deposito <=0:
#        print(f""" 
#                        Valor inválido.
#                    Operação não realizada.
#             """)
#    else:
#        saldo += valor_deposito
#        print(f""" 
#                    Depósito Efetuado
#                Saldo atual é de R${saldo:.2f}
#            """)
#        extrato =""
#        extrato += (f"Depósito                   R${valor_deposito:.2f}\n")
#    
#    return saldo , extrato

#
#def funcao_extrato(saldo,/,*,extrato):
#    if extrato is "":
#        print(f""" ===================================
# Não foram detectadas movimentações.
# =================================== """)
#    else:
#        print(extrato)
#        print(f"""===================================
#Saldo                      R${saldo:.2f}""")
#    
#def funcao_saque(*,valor_saque, saldo,numero_saques,saques_restantes,limite):
#    
#    
#    if valor_saque >500:
#        print(f""" 
#                        Operação inválida.
#                Valor excede o limite de saque.
#                    Limite de saque: R${limite:.2f}
#            """)
#            
#    elif valor_saque<=0:    
#         print(f""" 
#                      Valor inválido.
#                     Operação não realizada.
#                    Saldo Atual: R${saldo:.2f}
#            """)   
#
#    elif valor_saque > saldo:
#        print(f""" 
#                      Operação inválida.
#                    Valor excede o saldo.
#                    Saldo Atual: R${saldo:.2f}
#            """)
#            
#    else:
#        saldo-=valor_saque
#        numero_saques+=1
#        saques_restantes -=1
#        print(f""" 
#                        Saque realizado.
#                Quantidade de saques restantes:{saques_restantes}.
#                    Saldo atual: R${saldo:.2f}
#            """)
#        extrato=""
#        extrato += (f"Saque                      R${valor_saque:.2f}\n")
#
#        return saldo, numero_saques, saques_restantes, extrato 

def limpar_cpf(cpf): 
    cpf_limpo = "" 
    for char in cpf: 
        if char.isdigit(): 
            cpf_limpo += char 
    return cpf_limpo

def receber_data_nascimento(): 
    while True: 
        data_nascimento_input = input("Digite sua data de nascimento (dd/mm/yyyy)#: ")
        if len(data_nascimento_input) == 10 and data_nascimento_input[2] == '/' and data_nascimento_input[5] == '/': 
            dia, mes, ano = data_nascimento_input.split('/') 
            if dia.isdigit() and mes.isdigit() and ano.isdigit(): 
                dia = int(dia) 
                mes = int(mes) 
                ano = int(ano) 
                if 1 <= dia <= 31 and 1 <= mes <= 12: 
                    print("Data válida!") 
                    return data_nascimento_input 
                else: 
                    print("Dia ou mês inválido. Tente novamente.") 
            else: 
                print("Data inválida. Certifique-se de usar apenas números no #formato dd/mm/yyyy.") 
        else: 
            print("Formato inválido. Use o formato dd/mm/yyyy.")
            
def receber_endereco():
    print("Informe o endereço do cliente:")
    logradouro=input("Logradouro:")
    numero=input("Número:")
    bairro=input("Bairro:")
    cidade=input("Cidade:")
    estado=input("Estado:")
    endereco=[f"{logradouro},{numero}-{bairro}-{cidade}/{estado}"]
    return endereco

def receber_nome():
    nome=input("Digite o seu nome completo:")
    return nome
    
def cadastrar_clientes(cliente):
    while True:
        cpf_input = input("Digite o número do seu CPF:")
        if len(cpf_input) == 14 and cpf_input[3] =="." and cpf_input[7] == "." and cpf_input[11] == "-":
            cpf_limpo = limpar_cpf(cpf_input)
            print(f"cpf limpo: {cpf_limpo}")
            validar_cliente(clientes,cpf_input)
            # Se o CPF não estiver cadastrado, adicionar o novo cliente
            nome = receber_nome()
            data_de_nascimento = receber_data_nascimento()
            endereco = receber_endereco()
            clientes.append(PessoaFisica(endereco=endereco, cpf=cpf_limpo, nome=nome, data_nascimento=data_de_nascimento))
            #clientes.append([cpf_limpo, nome, data_de_nascimento, endereco])
            break
            #return cliente_cadastrado
        else:
            print("CPF INVÁLIDO - Use o formato XXX.XXX.XXX-XX.")
        

    

def validar_cliente(clientes,cpf):
    
    cpf_limpo = limpar_cpf(cpf)
    
    for cliente in clientes:
        
        if cliente.cpf == cpf_limpo:
            print("Cliente encontrado.")
            return cpf_limpo
        
    print("cliente não localizado")
    return ("erro")

def criar_conta(cpf,numero_conta):
    #conta = ContaCorrente(saldo=0.0, numero="001-1", agencia="0001", cliente=cliente, limite=500.0, limite_saques=3)
    
    numero_conta=numero_conta
    
    
    mensagem = f"Conta {AGENCIA}-{numero_conta} criada para o CPF: {cpf}"
    # Verificar se o CPF já existe no dicionário
    #if cpf in contas:
        # Adicionar uma nova conta ao CPF existente
    cliente_ativo=selecionar_cliente(cpf)
    conta = ContaCorrente(saldo=saldo,numero = numero_conta,agencia=AGENCIA,cliente=cliente_ativo, limite=limite,numero_saques=numero_saques)
    cliente_ativo.adicionar_conta(conta)
    #else:
        # Criar uma nova entrada para o CPF
    #    contas[cpf] = {f"conta_1": f"{AGENCIA}-{numero_conta}"}
    
    print(mensagem)
    numero_conta+=1
    return numero_conta

def menu_operacoes(): 
    while True:
        opcao = input(menu_conta)

        if opcao == "d":
            print("Depósito")
            #valor_deposito =0
            #valor_deposito += float(input("Digite o valor do depósito: R$"))
            #resultado_deposito = funcao_deposito(valor_deposito,saldo)
            #saldo=resultado_deposito[0]
            #extrato+=resultado_deposito[1]
        elif opcao == "s":
            print("Saque")
            #if numero_saques == LIMITE_SAQUES:
            #    print(f""" 
            #            Operação inválida.
            #    Quantidade de saques diária atingida.
            #        Quantidade de saques diários: {LIMITE_SAQUES}
            #""")
            #    continue
            #valor_saque = 0.0
            #valor_saque += float(input("Digite o valor do saque: R$"))
            #resultado_saque = funcao_saque(valor_saque=valor_saque,saldo=saldo,#numero_saques=numero_saques,#aques_restantes=saques_restantes,#limite=limite)
            #if resultado_saque == None:
            #    continue
            #else:
            #    saldo=resultado_saque[0]
            #    numero_saques=resultado_saque[1]
            #    saques_restantes=resultado_saque[2]
            #    extrato+=resultado_saque[3]
        elif opcao == "e":
            #print("               Extrato")
            #print("Tipo da Op. =============== Valor\n")
            #funcao_extrato(saldo,extrato=extrato)
            print("Histórico para fazer")
        elif opcao == "l":
            listar_contas()
        elif opcao == "q":
            break
        else: 
            print("Operação inválida, por favor selecione umas das operações #indicadas.")
            
def menu_cliente():
    global numero_conta
    while True:
        opcao = input(menu_usuario)
        if opcao == "n":
            cadastrar_clientes(clientes)
        elif opcao == "c":
            
            cpf_cliente_selecionado=input("Informe o CPF do cliente:")
            validar=validar_cliente(clientes,cpf_cliente_selecionado)
            if validar == "erro":
                print("cpf não localizado.")    
            else:
                criar_conta(validar,numero_conta)
                numero_conta+=1   
        elif opcao == "l":
            listar_clientes()
             
        elif opcao == "q":
            break
                     
def menu_inicial():
    
    while True:
        #print(menu_principal)
        opcao = input(menu_principal)
        if opcao == "c":
            menu_cliente()
        elif opcao == "o":
            menu_operacoes()
            #menu_operacoes()
        elif opcao == "q":
            break
        else:
            print("Opção inválida, selecione uma opção válida.")

clientes.append(PessoaFisica(endereco=["Rua tatata,80 - Vila 1 -São Paulo/SP"], cpf="20020020020", nome="Tatu", data_nascimento="10/10/1010"))
clientes.append(PessoaFisica(endereco=["Rua tatutua,90 - Vila 2 -São Paulo/SP"], cpf="10010010010", nome="Tata", data_nascimento="10/10/1010"))
clientes.append(PessoaFisica(endereco=["Rua tututua,10 - Vila 3 -São Paulo/SP"], cpf="00000000000", nome="Tata", data_nascimento="10/10/1010"))


contas.append(ContaCorrente(saldo=0.0,numero = 1,agencia=AGENCIA,cliente=clientes[0], limite=limite,numero_saques=numero_saques))
contas.append(ContaCorrente(saldo=0.0,numero = 2,agencia=AGENCIA,cliente=clientes[1], limite=limite,numero_saques=numero_saques))
contas.append(ContaCorrente(saldo=0.0,numero = 3,agencia=AGENCIA,cliente=clientes[2], limite=limite,numero_saques=numero_saques))
contas.append(ContaCorrente(saldo=0.0,numero = 4,agencia=AGENCIA,cliente=clientes[1], limite=limite,numero_saques=numero_saques))

def selecionar_cliente(cpf):
    for cliente in clientes:     
        #print(f"{index}: {cliente}")
        cpf_limpo=validar_cliente(clientes,cpf)
        if cliente.cpf == cpf_limpo:
            return (cliente)
def listar_clientes():
    for cliente in clientes: 
        print(cliente)
def listar_contas():
    print("listar contas:")
    for conta in contas: 
        print(conta)
    
       
menu_inicial()

