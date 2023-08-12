nome = input("Olá, informe seu nome! \n ==> ")

menu = f"""
================ Sistema Bancário DIO Potencia Tech - Ifood ================

Seja Bem-Vindo {nome.upper()}! a sua conta digital!

Qual operação deseja realizar?

[1] Depositar    [2] Sacar    [3] Extrato

[s] Sair

============================================================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            op = input(f"""
================ Sistema Bancário DIO Potencia Tech - Ifood ================

Depósito no valor de R${valor} realizado com sucesso!
      
Seu novo saldo atual é R$ {saldo}

============================================================================ 

Deseja realizar outra operação?

(qualquer tecla para continuar ou s para sair?)""")
            
            if op == "s":
              print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
              print(f"Obrigado pela preferência {nome.upper()}!\n")
              print("Desejamos um excelente dia!\n")  
              print("=============================== FIM ============================================\n")
              break 

        else:
            print("================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print("Operação falhou! O valor informado é inválido.\n")
            print("Escolha uma nova opção!\n")
            print("============================================================================\n")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print("Operação falhou! Você não tem saldo suficiente.\n")
            print("Escolha uma nova opção!\n")
            print("=============================== FIM ============================================\n")    

        elif valor > limite:
            print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print("Operação falhou! O valor do saque excede o limite.\n")
            print("Escolha uma nova opção!\n")
            print("=============================== FIM ============================================\n")

        elif numero_saques >= LIMITE_SAQUES:
            print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print("Operação falhou! Número máximo de saques excedido.\n")
            print("Escolha uma nova opção!\n")
            print("=============================== FIM ============================================\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.3f}\n"
            numero_saques += 1
            print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print(f"Saque no valor de R$ {valor} realizado com Sucesso!\n")
            print(f"Seu novo saldo e R$ {saldo} \n")
            print("=============================== FIM ============================================\n")

        else:
            print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
            print("Operação falhou! O valor informado é inválido\n")
            print("Escolha uma nova opção!\n")
            print("=============================== FIM ============================================\n")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================== F I M ==================")

    elif opcao == "s":
        print("\n================ Sistema Bancário DIO Potencia Tech - Ifood ================\n")
        print(f"Obrigado pela preferência {nome.upper()}!\n")
        print("Desejamos um excelente dia!\n")  
        print("=============================== FIM ============================================\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")