"""
Exercicios

Crie funções que duplicam, triplicam e quadruplicam
o numero recebido como parametro.
"""
def criar_multiplos(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplos(2)
triplicar = criar_multiplos(3)
quadruplicar = criar_multiplos(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4



