"""
Exercicio

Exiba os indices da lista
"""

lista = ['Maria', 'Felipe', 'Luiz']
lista.append('João')

indices = range(len(lista))

for i in indices:
    print(i, lista[i], type(lista[i]))



# for index, item in enumerate(lista):
#    print(index, item)
