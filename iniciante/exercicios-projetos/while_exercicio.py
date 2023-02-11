"""
Iterando strings com while
"""
nome = 'Felipe Soares' # 0 1 2 3 4 5 6 7 8 9 10 11 12
                       # F E L I P E   S O A R  E  S

tamanho_nome = len(nome)

# print(nome)
# print(tamanho_nome)
# print(nome[3])

indice = 0
novo_nome = ''

while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'

    indice += 1

novo_nome += '*'
print(novo_nome)
print('Acabou')