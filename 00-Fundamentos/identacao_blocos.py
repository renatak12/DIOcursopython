def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor
    
    print("Deposito realizado com sucesso")

sacar(1000)


print()

def sacar(valor):
    saldo = 500
    if valor <= saldo:
        print("valor sacado com sucesso")

    print("Tenha um bom dia!")

sacar(200)

def deposito(valor):
    saldo = 500
    if valor >= saldo:
        print("Deposito realizado com sucesso!")


deposito(500)