"""
Flag -> Marcar um local
None -> Não Valor
is e is not -> é ou não e (Tipo, Valor, Identidade)
id -> Identidade
"""

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1))
print('')
print(id(v2))
print('')
print(id(v3))

print('-' * 50)

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

else:
    print('Não passou no if')



