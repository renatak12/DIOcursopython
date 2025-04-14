# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)
print(not False)
print(not True)
print(not(True and False))
print(not(True or False))

print()

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # melhor forma
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

print()

print((5 > 3) and (2 < 4)) #T

print((10 == 10) or (5 != 5)) #T

print(not ((7 <= 7) and (3 > 1))) #F

print((True or False) and (False or False)) #F

print(not ((4 + 1 == 5) and (2 * 2 == 4))) #F
