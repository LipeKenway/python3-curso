"""
Exercício

Peça ao usuario para digitar seu nome
Peça ao usuario para digitar a idade

Se nome e idade forem digitados:

    Exiba:
        Seu Nome é {nome}
        Seu Nome invertido é {nome invertido}
        Se Nome contém (ou não) espaços
        Seu Nome tem {n} Letras
        A Primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
    Exiba "Desculpe, voce deixou o campo vazio"

"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

total_letras = len(nome)
ultima_letra = nome[-1::]
nome_invertido = nome[::-1]

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome_invertido}')
    print(f'Seu nome tem {total_letras} letras')
    print(f'A ultima letra do seu nome é {ultima_letra}')

    if ' ' in nome:
        print('Seu nome contém espaços')

    else:
        print('Seu nome não contém espaços')

else:
    print('Desculpe, um dos campos não foram preenchidos.')
    exit()
