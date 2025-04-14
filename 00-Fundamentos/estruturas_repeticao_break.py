# # Utilizando break e continue

# while True:

#     numero = int(input("Informe um número: "))

#     if numero == 10:
#         break            # Cortar a execução definitivamente
    
#     if numero % 2 == 0:
#         continue         # Para pular uma execução

#     print(numero)

# for numero in range(100):

#     if numero == 10:
#         break            # Cortar a execução definitivamente
    
#     if numero % 2 == 0:
#         continue         # Para pular uma execução

#     print(numero)

# Imprimir os múltiplos de 5 entre 1 e 50, mas parar se encontrar o 35  (exibe o 35)

for numeros in range(1,51):
    if numeros % 5 == 0:
        print(numeros)

    if numeros == 35:
        break

print()
# com while  (exibe o 35)
numeros = 1

while numeros <= 50:

    if numeros == 35:
        break
    if numeros % 5 == 0:
        print(numeros)
    numeros += 1

print()
# Pular a impressão dos múltiplos de 3 entre 1 e 30 

for number in range(1,31):
    if number % 3 == 0:
        continue
    print(number)

print()

number = 1

while number <= 30:
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1
