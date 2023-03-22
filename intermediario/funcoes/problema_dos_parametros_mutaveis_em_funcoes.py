"""
# Problema dos parametros mutaveis em funções Python
"""


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []

    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Luiz')
cliente1.append('Eduardo')
cliente1.append('Felipe')
cliente1.append('Maria')
cliente1.append('Marcos')


cliente2 = adiciona_clientes('Matheus')
cliente2.append('Vitor')
cliente2.append('Ana')

cliente3 = adiciona_clientes('Fernando')
adiciona_clientes('Carlos', cliente3)
adiciona_clientes('Ingrid', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
