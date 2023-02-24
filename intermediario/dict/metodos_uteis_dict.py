"""
Metodos uteis dos dicionarios em Python

* len() -> quantas chaves;
* keys() -> iteravel com as chaves;
* values() -> iteravel com os valores;
* items() -> iteravel com chaves e valores;
* setdefault() -> adiciona um valor se a chave não existe;
* copy() -> Retorna uma copia rasa (shallow copy);
* get() -> Obtem uma chave;
* pop() -> Apagar um item com a chave especificada (del);
* popitem() -> Apagar o ultimo item adicionado;
* update() -> Atualizar um dicionario com outro.
"""
import copy

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

# print(len(pessoa))

# print(list(pessoa.keys()))
# print(tuple(pessoa.keys()))

# print(pessoa.values())
# print(pessoa.items())

#pessoa.setdefault('tipo_sanguineo', 'Não informado')
# print(pessoa['tipo_sanguineo'])

# print(pessoa.get('nome'))
# print(pessoa.get('sobrenome', 'Não Existe'))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)

# pessoa.update({
#     'tipo_sanguineo': 'O+',
# })

# pessoa.update(nome='Maria', sobrenome='Cristina')

# tupla = (('nome', 'Maria'), ('idade', 30))
# lista = [['nome', 'Maria'], ['idade', 30]]
# pessoa.update(lista)
# print(pessoa)

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(d1)
# print(d2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# for valor in pessoa.values():
#     print(valor)

# for chave in pessoa.keys():
#     print(chave)
