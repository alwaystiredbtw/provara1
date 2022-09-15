# -------------- # 
# consultar saldo, saque, deposito, sair # 

from glob import glob
from timeit import repeat


saldo = 0.0
operacao = 0
valorS = 0          #valor saque
valorD = 0          #valor deposito


def menu():
    print("Qual operacao deseja realizar?\n1 - Consultar saldo\n2 - Saque\n3 - Deposito\n4 - Sair")
    operacao = int(input(":"))
    return operacao
def saque():
    global saldo
    valorS = float(input("Qual o valor do saque que deseja realizar?"))
    if saldo == 0.0:
        print("Voce nao tem saldo, impossivel realizar saque!")
    if saldo < valorS:
        print(f"Seu saldo eh de apenas R${saldo}, nao eh possivel realizar saque")
    if saldo > valorS:
        saldo -= valorS
        print(f"Realizando saque de R${valorS} !")
        print(f"Seu novo saldo eh {saldo}")
def deposito():
    global saldo
    global valorD
    valorD = float(input("Qual o valor do deposito?"))
    saldo += valorD
    print(f"Seu novo saldo eh R${saldo}")






while True:
    operacao = menu()
    match operacao:
        case 1:
            print(f"Seu saldo eh {saldo}")
        case 2:
            saque()
        case 3:
            deposito()
        case 4:
            break

print("Obrigado por usar o sistema!")

            
    

