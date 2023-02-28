"""
Função lambda em Python PT. 2
"""

def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar

duplica = executa(
    lambda m: lambda n: n * m, 
    2
)

print(duplica(2))

print(
    executa(
        lambda x, y: x + y, 
        2, 3
    ),
)

print(executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)