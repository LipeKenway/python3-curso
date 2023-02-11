"""
Faça um jogo para o usuario advinhar qual é a palavra secreta.

-> Vc vai propor uma palavra secreta qualquer e vai dar a possibili- dade para o usuario digitar apenas uma letra.

-> Quando o usuario digita uma letra, vc vai conferir se a letra digitada esta na palavra secreta.

-> Se a letra digitada estiver na palavra secreta, exiba a letra.
-> Se a letra digitada não estiver na palavra secreta, exiba.

-> Faça uma contagem de tentativas do seu usuario.

"""
palavra_secreta = 'arroz'
tamnaho_plvra_secreta = len(palavra_secreta)

tentativas = 0
letras_acertadas = ''

while True:
    letra_usuario = input('Digite apenas uma letra: ').lower()
    tentativas += 1
    letra_eh_digito = letra_usuario.isdigit()

    if letra_eh_digito:
        print('Por favor, digite apenas letras não numeros.')
        continue

    if not letra_eh_digito:

        if len(letra_usuario) > 1:
            print('Por Favor, digite apenas uma letra.')
            continue
        
        if letra_usuario in palavra_secreta:
            letras_acertadas += letra_usuario
            
        palavra_formada = ''
            
        for letra in palavra_secreta:
            if letra in letras_acertadas:
                palavra_formada += letra
            else:
                palavra_formada += '*'

        print(palavra_formada)
        print('-' * 50)

        if palavra_formada == palavra_secreta:
            print('PARABENS, VOCE ACERTOU A PALAVRA SECRETA !!!')
            print(f'A palavra era "{palavra_secreta.capitalize()}".')
            print(f'Tentativas: {tentativas}x')
            print('')
            break
        
                
