"""
Cuidados com dados mutaveis

= - copiado o valor (imutaveis).
= - aponta para o mesmo valor na memoria (mutavel).
"""

nome = 'Felipe'
outra_variavel = nome

nome = 'Luiz'
# print(nome)
# print(outra_variavel)

lista_a = ['Luiz', 'Felipe']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print('Lista A =', lista_a)
print('Lista B =', lista_b)



