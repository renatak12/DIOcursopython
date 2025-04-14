# opcao = -1

# while opcao != 0:
    
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
#     if opcao == 1:
#         print("Sacando seu dinheiro...")
        
#     elif opcao == 2:
#         print("Exibindo extrato...")

# print("Obrigado por usar nosso sistema bancario, até logo.")

#1 Imprimir os números pares de 0 a 20 usando
numero = 0

while numero <= 20:
    if numero % 2 == 0:
        print(numero)
    numero += 1

#2 Exemplo sem if
numero = 0

while numero <= 20:
    print(numero)
    numero += 2

# Exercicio 3
soma = 0
numero = 1

while numero <= (100):
    soma += numero
    numero += 1

print("A soma dos números de 1 a 100 é:", soma)

#4 (meu codigo)Exercicio - Pedir ao usuário números até ele digitar 0
numero = 1

while numero != 0:
    print("Você digitou:", numero)
    numero= int(input("Informa um número: "))

print("0 sai do programa")

# versão 2
numero = int(input("Informe um número (0 para sair): "))

while numero != 0:
    print("Você digitou:", numero)
    numero = int(input("Informe outro número (0 para sair): "))

print("Você digitou 0. Programa encerrado!")

#Contar quantos números ímpares existem entre 1 e 100
numero = 1

while numero <= 100:
    if numero % 2 == 1:
        print(numero)
    numero += 1

print()
# exemplo com contador 
numero = 1
contador = 0

while numero <= 100:
    if numero % 2 == 1:
        contador += 1
    numero += 1

print("Quantidade de números ímpares entre 1 e 100:", contador)

# TO DO Criar um contador regressivo de 10 até 0 usando while
