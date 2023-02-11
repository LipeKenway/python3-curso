"""
* Faça um programa que peça ao usuario para digitar um numero inteiro;
* Informe se este numero eh par ou impar. 
* Caso o usuario nao digite um numero inteiro, informe que nao eh um numero inteiro.
"""
entrada = input("Digite um numero inteiro: ")

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0

    if par_impar:
        print(f'O Numero {entrada_int} é um numero par.')

    else:
        print(f'O Numero {entrada_int} é um numero impar.')

except:

    print('Isso não eh um numero inteiro.')








