"""
! Exercicios

* 1) Exercicio
-> Aumente os preços dos produtos a seguir em 10%
-> Gere novos_produtos por deep copy (cópia profunda)

* 2) Exercicio
-> Ordene os produtos por nome decrescente (do maior para o menor).
-> Gere produtos_ordenados_por_nome por deep copy (cópia profunda).

* 3) Exercicio
-> Ordene os produtos por preço crescente (do menor para o maior).
-> Gere produtos_ordenados_por_preco por deep copy (cópia profunda).
"""
from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 4', 'preco': 23.50},
    {'nome': 'Produto 1', 'preco': 50.42},
    {'nome': 'Produto 3', 'preco': 36.15},
    {'nome': 'Produto 2', 'preco': 42.67},
]



