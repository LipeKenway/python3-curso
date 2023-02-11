"""
* Faça um programa que peça o primeiro nome do usuario.
* Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; 
* Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; 
* Maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Informe seu primeiro nome: ')

try:
    tamanho_nome = len(nome)
    limite_nome = tamanho_nome <= 1
    total_letras_nome = tamanho_nome
    
    curto = total_letras_nome > 2 and total_letras_nome <= 4
    normal = total_letras_nome >= 5 and total_letras_nome <= 6
    grande = total_letras_nome > 6

    nome_eh_int = nome.isdigit()
    nome_nao_int = not nome.isdigit()

    if nome_eh_int:
        print('Por favor, digite apenas letras.')
    
    else:
        ...

    if nome_nao_int:
        
        if limite_nome:
            print('Por favor, digite mais de uma letra.')

        elif curto:
            print('Seu nome é curto.')
    
        elif normal:
            print('Seu nome é normal.')

        elif grande:
            print('Seu nome é muito grande.')

except:
    print('Desculpe, você informou algo errado.')
