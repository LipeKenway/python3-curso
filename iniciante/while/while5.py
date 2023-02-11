"""
Repetições

while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
"""

linha = 1

qtd_linhas = 2
qtd_colunas = 5

while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'linha: {linha} | coluna: {coluna}')
        coluna += 1

    linha += 1

print('-' * 20)
print('Acabou')