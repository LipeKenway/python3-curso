"""
# Groupby -> Agrupando Valores (Itertools).
"""
from itertools import groupby

alunos = [
    {'nome': 'Marcos', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'E'},
    {'nome': 'Pedro', 'nota': 'D'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Felipe', 'nota': 'C'},
    {'nome': 'Luiz', 'nota': 'F'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Elisa', 'nota': 'D'},
    {'nome': 'Anderson', 'nota': 'A'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)