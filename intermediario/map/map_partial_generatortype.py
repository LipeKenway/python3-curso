"""
# Map -> Mapear dados
"""
from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
produtos = [
    {'nome': 'Produto 4', 'preco': 10.99},
    {'nome': 'Produto 1', 'preco': 50.20},
    {'nome': 'Produto 5', 'preco': 26.11},
    {'nome': 'Produto 3', 'preco': 75.40},
    {'nome': 'Produto 2', 'preco': 15.24},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p, 
#         'preco': aumentar_dez_porcento(p['preco'])} 
#     for p in produtos
# ]

def muda_preco_produto(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

novos_produtos = list(map(muda_preco_produto, produtos))

#print_iter(produtos)
print_iter(novos_produtos)

print(list(map(lambda x: x * 3, [1, 2, 3 ,4])))

# print(novos_produtos)
# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))
# print(isinstance(novos_produtos, GeneratorType))
