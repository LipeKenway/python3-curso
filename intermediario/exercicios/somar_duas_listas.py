"""
Considerando duas listas de inteiros ou floats (l1, l2).

Some os valores nas listas retornando uma nova lista 
com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar
o tamanho da menor.

Ex.:
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
===========================
lista_somada = [2, 4, 6, 8]
"""
from itertools import zip_longest

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

lista_somada = [(x + y) for x, y in zip(l1, l2)]
lista_somada2 = [(x + y) for x, y in zip_longest(l1, l2, fillvalue=0)]
print(lista_somada)
print(lista_somada2)
