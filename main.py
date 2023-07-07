menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: +{valor_deposito}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                extrato += f"Saque: -{valor_saque}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")
            elif valor_saque > limite:
                print("Limite de saque excedido.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "e":
        print(f"Extrato:\n{extrato}Saldo atual: {saldo}")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Digite novamente.")