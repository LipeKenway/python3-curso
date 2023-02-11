frase = 'O Python é uma linguagem de programação multiparadigma.\n'\
        'Python foi criado por Guido van Rossum.'

i = 0
qtd_letras_mais_repetidas = 0
letra_mais_repetida = ''

while i < len(frase):
    
    letra_atual = frase[i]

    if letra_atual == ' ':
        i+=1
        continue

    qtd_letras_atuais = frase.count(letra_atual)

    if qtd_letras_mais_repetidas <= qtd_letras_atuais:
        qtd_letras_mais_repetidas = qtd_letras_atuais
        
        letra_mais_repetida = letra_atual

    i+=1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_repetida}" que apareceu '
    f'{qtd_letras_mais_repetidas}x'
)