menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)
    

    if opcao == "1":
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
        
    
    elif opcao == "2":
        saque = float(input("Digite o valor a ser sacado: "))
        if saldo < saque:
            print("Saldo insuficiente")
        elif saque > limite:
            print("Limite de saque excedido")
        elif numero_saque >= LIMITE_SAQUES:
            print("Número de saques diários excedido.")
        elif saldo >= saque:
            saldo -= saque
            numero_saque += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("Saque realizado.")
        else:
            print("Valor inválido para saque.")

    elif opcao == "3":
        print("\n=========== EXTRATO ===========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "0":
        print("Saindo... Obrigada por usar o sistema 💰")
        break

    else:
        print("Operação invalida, por favor selecionar novamente a operação desejada.")