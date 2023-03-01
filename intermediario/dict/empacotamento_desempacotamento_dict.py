"""
Empacotamento e Desempacotamento de Dicionarios
"""
a, b = 1, 2
a, b = b, a

# print(a, b)


# a, b = pessoa.values()
# print(a, b)
# print('-' * 50)

# a, b = pessoa.items()
# print(a, b)
# print('-' * 50)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print('-' * 50)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.7,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

def mostro_args_nomeados(*args, **kwargs):
    print('Não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_args_nomeados(1, 2, nome='Joana', qlq=123)
# mostro_args_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_args_nomeados(**configuracoes)

# args e kwargs
# args -> (argumentos não nomeados)
# kwargs -> keyword arguments (argumentos nomeados)