"""
# Reduce -> Faz a redução de um iteravel em um valor.
"""
from functools import reduce


produtos = [
    {'nome': 'Produto 4', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 50},
    {'nome': 'Produto 5', 'preco': 26},
    {'nome': 'Produto 3', 'preco': 75},
    {'nome': 'Produto 2', 'preco': 15},
]

# def total_somado(acumulador, produto):
#     print('acumulador:', acumulador)
#     print('produto:', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print('O Total é ', total)

# for p in produtos:
#     total += p['preco']

# print(total)