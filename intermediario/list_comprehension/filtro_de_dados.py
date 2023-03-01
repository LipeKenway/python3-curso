"""
Filtro de dados com list comprehension
"""
import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 60,},
    {'nome': 'p3', 'preco': 50,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 20
    ]

p(novos_produtos)

# print(*novos_produtos, sep='\n')
# lista = [n for n in range(10) if n < 5]
# print(lista)


