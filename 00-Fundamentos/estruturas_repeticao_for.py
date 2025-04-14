# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"


# # Exemplo de repetição usando um iteravel.
# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")

# print()

# # Exemplo de repetição usando a função built-in range.
for numero in range(0,16,2):
    print(numero, end="")

print()

# Imprimir os números de 1 a 10 

for numero in range(1,11):
    print(numero)

# Calcular a soma dos números de 1 a 100 
soma = 0

for numero in range(1, 101):
    soma += numero

print("A soma dos números de 1 a 100 é:", soma)

#Imprimir a tabuada de um número digitado pelo usuário

numero = int(input("Informa um numero para ver a tabuada: "))

print(f"A tabuada de {numero} é:")

for i in range(1,11):

    resultado = i * numero
    print(f"{numero} x {i} = {resultado} ")

#Contar quantos números ímpares existem entre 1 e 100

for i in range(1,101):
    if i % 2 == 1:
        print(i)

print()
# exemplo com contador para informa a quantidade exata de numeros impares.
contador = 0

for i in range(1, 101):
    if i % 2 == 1:
        contador += 1

print("Quantidade de números ímpares entre 1 e 100:", contador)


#TO DO Desenhar um triângulo com for