import copy
from pprint import pprint

produtos = [
    {'nome': 'Produto 5', 'preco': 36.15},
    {'nome': 'Produto 4', 'preco': 23.50},
    {'nome': 'Produto 1', 'preco': 42.67},
    {'nome': 'Produto 3', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 50.42},
]

def aumento_de_preco(produtos):
    
    for produto in produtos:
        
        aumento_preco = float("{:.2f}".format(produto['preco'] * 1.1))
        
        produto['preco'] = aumento_preco 
        
    return produtos

def nome_decrescente():
     nome_ordenado = sorted(aumento_de_preco(produtos), key=lambda nome: nome['nome'], reverse=True)
     return nome_ordenado

def preco_crescente():
     preco_ordenado = sorted(aumento_de_preco(produtos), key=lambda preco: preco['preco'])
     return preco_ordenado

pprint(aumento_de_preco(produtos))
#pprint(nome_decrescente())
#pprint(preco_crescente())