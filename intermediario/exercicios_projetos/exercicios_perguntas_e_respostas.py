"""
Exercicio - Sistema de perguntas e respostas
"""
import os
from time import sleep


perguntas = [
    {
        'pergunta': 'Quanto eh 2 + 2 ?',
        'opcoes': ['2', '4', '5', '1', '3'],
        'resposta' : '4',
    },
    {
        'pergunta': 'Quanto eh 5 x 2 ?',
        'opcoes': ['20', '25', '15', '10', '50'],
        'resposta' : '10',
    },
    
    {
        'pergunta': 'Quanto eh 10 / 2 ?',
        'opcoes': ['5', '2', '9', '10', '4'],
        'resposta' : '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print(f'Pergunta:', pergunta['pergunta'])
    print()

    opcoes = pergunta['opcoes']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    qtd_opcoes = len(opcoes)
    qtd_perguntas = len(perguntas)

    acertou = False
    resposta_int = None
    resposta_usuario = input('Escolha uma das alternativa: ')
    print()
    
    if resposta_usuario.isdigit():
        resposta_int = int(resposta_usuario)
    else:
        print('Desculpe isso não eh uma alternativa valida.')
        break

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['resposta']:
                acertou = True
        else:
            print('Desculpe, mas essa opção não esta entre as alternativas da pergunta.')     
            break  

    if acertou:
        print('Resposta Certa !!!')
        qtd_acertos += 1
        print()

    else:
        print('Resposta Errada !!!')
        print()
    
    sleep(2)
    os.system('cls')
    continue

print(f'Você acertou {qtd_acertos} das {qtd_perguntas} perguntas.')

                 


    
    



