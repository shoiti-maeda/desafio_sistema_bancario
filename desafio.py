menu="""  
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
==> """

saldo = 0.0
limite = 500.0
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3
saques_restantes = LIMITE_SAQUES

def funcao_deposito(valor_deposito,saldo):
        
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
        extrato =""
        extrato += (f"Depósito                   R${valor_deposito:.2f}\n")
    
    return saldo , extrato


def funcao_extrato(extrato,saldo):
    if extrato is "":
        print(f""" ===================================
 Não foram detectadas movimentações.
 =================================== """)
    else:
        print(extrato)
        print(f"""===================================
Saldo                      R${saldo:.2f}""")
    
    
    

def funcao_saque(valor_saque, saldo,numero_saques,saques_restantes):
    
    
    if valor_saque >500:
        print(f""" 
                        Operação inválida.
                Valor excede o limite de saque.
                    Limite de saque: R${limite:.2f}
            """)
            
    elif valor_saque<=0:    
         print(f""" 
                      Valor inválido.
                     Operação não realizada.
                    Saldo Atual: R${saldo:.2f}
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
        saques_restantes -=1
        print(f""" 
                        Saque realizado.
                Quantidade de saques restantes:{saques_restantes}.
                    Saldo atual: R${saldo:.2f}
            """)
        extrato=""
        extrato += (f"Saque                      R${valor_saque:.2f}\n")

        return saldo, numero_saques, saques_restantes, extrato 

    
while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito =0
        valor_deposito += float(input("Digite o valor do depósito: R$"))
        resultado_deposito = funcao_deposito(valor_deposito,saldo=saldo)
        saldo=resultado_deposito[0]
        extrato+=resultado_deposito[1]


    elif opcao == "s":
        print("Saque")
        if numero_saques == LIMITE_SAQUES:
            print(f""" 
                       Operação inválida.
              Quantidade de saques diária atingida.
                Quantidade de saques diários: {LIMITE_SAQUES}
           """)
            continue
        valor_saque = 0.0
        valor_saque += float(input("Digite o valor do saque: R$"))
        resultado_saque = funcao_saque(valor_saque, saldo,numero_saques,saques_restantes)
        saldo=resultado_saque[0]
        numero_saques=resultado_saque[1]
        saques_restantes=resultado_saque[2]
        extrato+=resultado_saque[3]
    
    elif opcao == "e":
        print("               Extrato")
        print("Tipo da Op. =============== Valor\n")
        funcao_extrato(extrato,saldo)

    elif opcao == "q":
        break
    else: 
        print("Operação inválida, por favor selecione umas das operações indicadas.")

