# Exemplo 1 com upper, lower e title (maximo,minimo e titulo)

nome = "AmAnDa"


print(nome.upper())
print(nome.lower())
print(nome.title())

# Exemplo 2 com strip (para retirar os espaços vazios)
texto = "   Olá mundo!    "


print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

# Exemplo 3 com center e join
menu = "python"


print(menu.center(14))
print(menu.center(14, "."))
print("-".join(menu))