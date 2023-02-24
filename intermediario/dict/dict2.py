"""
Manipulando chaves e valores em dicionarios
"""
pessoa = {}

chave = 'nome'
pessoa[chave] = 'Felipe'
pessoa['sobrenome'] = 'Soares'


print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']

print(pessoa)
print('-' * 50)

if pessoa.get('sobrenome') is None:
    print('Não existe.')
else:
    print(pessoa['sobrenome'])


