import textwrap

def menuconta():
    menuconta_text = """
    ======= MENU =======

    1 - Deposito
    2 - Saque
    3 - Extrato
    4 - Novo Usuario
    5 - Nova Conta
    6 - Listar contas
    7 - Sair

   ====================
    \n"""    
    return input(textwrap.dedent(menuconta_text))

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}\n")
        print(f"\nO depósito no valor de R$ {valor:.2f} foi realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        print(f"\nO saque no valor de R$ {valor:.2f} foi realizado com sucesso!")
        extrato.append(f"Saque: R$ {valor:.2f}\n")
        numero_saques += 1
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print('='*15 + ' EXTRATO ' + '='*15)
    print("\nNão foram realizadas movimentações." if not extrato else ''.join(extrato))
    print(f"\nSaldo: R$ {saldo:.2f}")
    print('='*39)

def criar_usuario(usuarios):
    nome = input("Nome do usuário: ")
    data_nascimento = input("Data de nascimento (DD-MM-AAAA): ")
    while True:
        cpf = input("CPF: ")
        
        # Verificar se todos os caracteres do CPF são dígitos
        if not cpf.isdigit():
            print("CPF inválido. O CPF deve conter apenas números.")
            continue

         # Verificar se o CPF tem 11 dígitos
        if len(cpf) != 11:
            print("CPF inválido. O CPF deve conter 11 dígitos.")
            continue
        break
  
    # Verificar se o CPF já existe na lista de usuários
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário cadastrado com este CPF.")
            return

    # Armazenar apenas os números do CPF
    cpf = ''.join(c for c in cpf if c.isdigit())

    endereco = input("Endereço (logradouro, numero - bairro - cidade - estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")
    return True

def criar_conta(contas, usuarios, agencia):  # Adicionando 'agencia' como argumento
    numero_conta = len(contas) + 1

    # Solicitar o CPF do usuário para vincular à conta
    cpf_usuario = input("Digite o CPF do usuário para vincular à conta: ")

    # Verificar se o CPF é válido e se corresponde a um usuário na lista
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado is None:
        print("Usuário não encontrado. Verifique o CPF e tente novamente.")
        return

    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_encontrado}
    contas.append(conta)
    print("Conta corrente criada com sucesso!")

def listar_contas(contas):
    print("Listagem de contas:")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao_conta = menuconta()

        if opcao_conta == "1":
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao_conta == "2":
            valor = float(input("\nInforme o valor do saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao_conta == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao_conta == "4":
            criar_usuario(usuarios)
                 
        elif opcao_conta == "5":
            criar_conta(contas, usuarios, AGENCIA)

        elif opcao_conta == "6":
            listar_contas(contas)

        elif opcao_conta == "7":
            print("\nObrigado por utilizar os nossos serviços!\n") 
            exit()

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

main()
