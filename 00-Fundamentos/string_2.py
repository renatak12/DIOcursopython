nome = "Renata"
idade = 30
Profissao = "Programadora"
linguagem = "Python"

saldo = 50.151
dados = {"nome": "Renata", "idade": 30}

print("Meu nome é %s e minha idade é %d" %(nome,idade)) # pouco usado

print("Meu nome é {} e minha idade é {}".format(nome,idade))
print("Meu nome é {1} e minha idade é {0}".format(idade,nome))
print("Meu nome é {nome} e minha idade é {idade}".format(nome=nome,idade=idade))
print("Meu nome é {nome} e minha idade é {idade}".format(nome=nome,idade=idade))

print("Meu nome é {nome} e minha idade é {idade}".format(**dados))

print(f"Meu nome é {nome} e minha idade é {idade}")
print(f"Meu nome é {nome} e minha idade é {idade} e meu saldo é {saldo}")
print(f"Meu nome é {nome} e minha idade é {idade} e meu saldo é {saldo:.1f}")
