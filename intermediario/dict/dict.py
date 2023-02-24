"""
Dicionarios em Python (Tipo dict())

Dicionarios são estruturas de dados do tipo par de "chave" e "valor".

Chaves podem ser consideradas como o indice que vimos na lista e podem
ser de tipos imutaveis como: str, int, float, bool, tuple, etc...

O valor pode ser de qualquer tipo, incluindo outro dicionario.

Usamos as chaves {} ou a classe dict() para criar dicionarios.

Imutaveis -> str, int, float, bool, tuple
Mutaveis -> dict(), list()
"""
pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Soares',
    'idade': 24,
    'altura': 1.80,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
