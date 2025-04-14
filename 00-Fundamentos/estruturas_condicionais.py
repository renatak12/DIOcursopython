MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode tirar sua CNH.")
else:
    print("Você não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Você pode tirar sua CNH.")
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aula teoricas, mas não pode fazer as aulas práticas.")
else:
    print("Você não pode tirar a CNH")