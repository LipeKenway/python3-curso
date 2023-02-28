"""
Função lambda em Python

* A função lambda é uma função como qualquer outra em Python.
* Porém, são funções anonimas que contem apenas uma linhas.
* Ou seja, tudo deve ser contido dentro de uma unica expressão.
"""

# lista = [4, 3, 7, 1, 10, 59, 22, 16, 9]
# lista.sort()
# sorted(lista)

lista = [
    {'nome': 'Felipe', 'sobrenome': 'Soares'},
    {'nome': 'Carla', 'sobrenome': 'Mendes'},
    {'nome': 'João', 'sobrenome': 'Oliveira'},
    {'nome': 'Pedro', 'sobrenome': 'Miranda'},
    {'nome': 'Ana', 'sobrenome': 'Padua'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)