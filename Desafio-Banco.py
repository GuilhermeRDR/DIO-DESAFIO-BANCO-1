menu = """
===== MENU =====

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    escolha = input(menu)

    if escolha == "1":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"\nO depósito no valor de R$ {valor:.2f} foi realizado com sucesso!")

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif escolha == "2":
        valor = float(input("\nInforme o valor do saque: "))

        if valor > saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("\nOperação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            print(f"\nO saque no valor de R$ {valor:.2f} foi realizado com sucesso!")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nOperação falhou! O valor informado é inválido.")


    elif escolha == "3":
        print('='*15 + ' EXTRATO ' + '='*15)
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('='*39)

    elif escolha == "4":
        print("\nObrigado por ultilizar os nossos serviços!\n") 
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
