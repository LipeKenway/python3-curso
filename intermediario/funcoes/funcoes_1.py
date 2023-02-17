"""
Introdução as funçôes (def) em Python

Funções são trochos de codigo usados para
replicar determinada ação ao longo do seu codigo.

Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.

Por padrão, funções Python retornam None (nada).
"""

# def Print():
#    print('Varias 1')
#    print('Varias 2')
#    print('Varias 3')
#    print('Varias 4')


# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem Nome'):
    print(f'Olá, {nome}!')

saudacao('Felipe')
saudacao('Maria')
saudacao('Luiz')
saudacao()