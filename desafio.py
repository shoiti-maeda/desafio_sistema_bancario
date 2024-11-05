menu="""  
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
==> """

saldo = 0.0
limite = 500.0
extrato = "Tipo da Op. ========== Valor\n"
numero_saques = 0
LIMITE_SAQUES = 3
limite_saques_restantes = LIMITE_SAQUES
valor_saque = 0.0
valor_deposito = 0.0

def funcao_deposito():
    global saldo
    global extrato
    global valor_deposito
    valor_deposito=0
    valor_deposito += float(input("Digite o valor do depósito: R$"))
    if valor_deposito <=0:
        print(f""" 
                        Valor inválido.
                    Operação não realizada.
             """)
    else:
        saldo += valor_deposito
        print(f""" 
                    Depósito Efetuado
                Saldo atual é de R${saldo:.2f}
            """)
        extrato += (f"Depósito               R${valor_deposito:.2f}\n")


def funcao_extrato():
    global extrato
    print(extrato)
    print(f"""===================================
Saldo                  R${saldo:.2f}""")
    
    
    

def funcao_saque():
    global saldo
    global extrato
    global numero_saques
    global valor_saque
    global limite_saques_restantes
    valor_saque = 0.0
    valor_saque += float(input("Digite o valor do saque: R$"))
    if valor_saque >500:
        print(f""" 
                        Operação inválida.
                Valor excede o limite de saque.
                    Limite de saque: R${limite:.2f}
            """)
            
        
            

    elif valor_saque > saldo:
        print(f""" 
                      Operação inválida.
                    Valor excede o saldo.
                    Saldo Atual: R${saldo:.2f}
            """)
            
    else:
        saldo-=valor_saque
        numero_saques+=1
        limite_saques_restantes -=1
        print(f""" 
                        Saque realizado.
                Quantidade de saques restantes:{limite_saques_restantes}.
                    Saldo atual: R${saldo:.2f}
            """)
        extrato += (f"Saque                  R${valor_saque:.2f}\n")

    
while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        funcao_deposito()

    elif opcao == "s":
        print("Saque")
        if numero_saques == LIMITE_SAQUES:
            print(f""" 
                       Operação inválida.
              Quantidade de saques diária atingida.
                Quantidade de saques diários: {LIMITE_SAQUES}
           """)
            continue
        funcao_saque()
    
    elif opcao == "e":
        print("Extrato")
        funcao_extrato()

    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione umas das operações indicadas.")

