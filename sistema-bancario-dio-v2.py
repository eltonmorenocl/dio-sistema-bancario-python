def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
        print(f"Seu novo saldo atual é R$ {saldo}\n")
        print("=============================== FIM ============================================\n")
    else:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Operação falhou! O valor informado é inválido.")
        print("Escolha uma nova opção!\n")
        print("=============================== FIM ============================================\n")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    
    if valor > saldo:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Operação falhou! Você não tem saldo suficiente.")
        print("=============================== FIM ============================================\n")
    elif valor > limite:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Operação falhou! O valor do saque excede o limite.")
        print("=============================== FIM ============================================\n")
    elif numero_saques >= LIMITE_SAQUES:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Operação falhou! Número máximo de saques excedido.")
        print("=============================== FIM ============================================\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.3f}\n"
        numero_saques += 1
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print(f"Saque no valor de R$ {valor} realizado com sucesso!")
        print(f"Seu novo saldo é R$ {saldo}\n")
        print("=============================== FIM ============================================\n")
    else:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Operação falhou! O valor informado é inválido.")
        print("Escolha uma nova opção!\n")
        print("=============================== FIM ============================================\n")
    
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("================== F I M ==================")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Operação falhou! Já existe usuário com esse CPF!")
        print("\n=============================== FIM ============================================\n")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
    print("Usuário criado com sucesso!")
    print("\n=============================== FIM ============================================\n")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print("Conta criada com sucesso!")
        print("\n=============================== FIM ============================================\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
    print("Operação falhou! Usuário não encontrado!")
    print("\n=============================== FIM ============================================\n")

def listar_contas(contas):
    for conta in contas:
        print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)
        print("=" * 100)

def main():
    nome = input("Olá, informe seu nome!\n==> ")
    menu = f"""
    ================= Sistema Bancário DIO Potencia Tech - Ifood ================

    Seja Bem-Vindo {nome.upper()}! A sua conta digital!

    Qual operação deseja realizar?

    [1] Depositar    [2] Sacar      [3] Extrato

    [4] Novo Usuário [5] Nova Conta [6] Listar Contas
        
    [s] Sair

    ============================================================================\n=> """
    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        
        elif opcao == "3":
            mostrar_extrato(saldo, extrato)
        
        elif opcao == "4":
            novo_usuario(usuarios) 
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            result = nova_conta(AGENCIA, numero_conta, usuarios)
            if result:
                contas.append(result)
        
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "s":
            print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print(f"Obrigado pela preferência {nome.upper()}!")
            print("Desejamos um excelente dia!\n")
            print("\n=============================== FIM ============================================\n")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
