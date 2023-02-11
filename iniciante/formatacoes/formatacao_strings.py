"""
# F-Strings
"""

nome = 'Felipe Soares'
altura = 1.80
peso = 90
imc = peso / altura ** 2

linha1 = f'{nome} tem {altura:.2f} de altura, '
linha2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha1)
print(linha2)