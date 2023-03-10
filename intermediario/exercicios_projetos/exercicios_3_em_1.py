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
from dados.produtos_modulos import produtos

import copy
from pprint import pprint

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
    ]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'], reverse=True
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['preco']
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')









    
   