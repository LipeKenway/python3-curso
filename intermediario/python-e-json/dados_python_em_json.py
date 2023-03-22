"""
# Salvando dados Python em JSON
"""
import json

caminho_arquivo = 'C:\\Users\\lyppy\\Downloads\\Cursos\\python\\intermediario\\python-e-json\\'
caminho_arquivo += 'dados_python_em_json.json'

# pessoa = {
#     'nome': 'Felipe',
#     'sobrenome': 'Soares',
#     'endereco': [
#         {'rua': 'R1', 'numero': 111},
#         {'rua': 'R2', 'numero': 256}
#     ],
#     'altura': 1.8,
#     'numero_preferido': (2, 7, 11),
#     'dev': True,
#     'nada': None
# }

# with open(caminho_arquivo, 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open(caminho_arquivo, 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'], pessoa['sobrenome'])

    # print(pessoa)
    # print(type(pessoa))
