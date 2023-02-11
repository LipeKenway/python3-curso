"""
enumerate -> Enumera iteraveis (indices)
"""

nomes = ['Felipe', 'Maria', 'Luiz']
nomes.append('João')

# [(0, 'Felipe'), (1, 'Maria'), (2, 'Luiz'), (3, 'João')]
# nomes_enumerados = list(enumerate(nomes))
# print(nomes_enumerados)

# for indice, item in enumerate(nomes):
#    print(indice, item)

for tupla_enumerada in enumerate(nomes):
    print('FOR da tupla: ')

    for valor in tupla_enumerada:
        print(f'\t{valor}')