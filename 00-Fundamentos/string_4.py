# String multiplas linhas

nome = "Guilherme"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

    Obrigado por usar nosso sistema!!!!
"""
)

texto = """
Amor é fogo que arde sem se ver
É ferida que dói e não se sente
É um contentamento descontente
É dor que desatina sem doer
"""

# 1. Contar linhas
# 2. Contar palavras
# 3. Mostrar texto em maiúsculas
# 4. Substituir 'amor' por 'carinho'

linhas = texto.splitlines()
quantidade_de_linhas = len(linhas)

print("Quantidade de linhas:", quantidade_de_linhas)


palavras = texto.split()
quantidade_de_palavras = len(palavras)

print("Quantidade de palavras: ", quantidade_de_palavras)

texto_em_maiusculo = texto.upper()

print("Texto: ", texto_em_maiusculo)

trocar_palavras = texto.replace("Amor","Carinho").replace("amor", "carinho")

print("Texto com palavras trocadas: ", trocar_palavras)