"""
Exercicios com funções

* Crie uma função que multiplica todos os argumentos não nomeados.
* Retorne o total para uma variavel e mostre o valor da variavel.

* Crie uma função que fala se um numero é par ou impar.
* Retorne se o numero é par ou impar.
"""
def multiplicacao(*args):
    total = 1

    for numero in args:
        total *= numero
    return total

numero_multiplicado = 4, 5, 10
print(multiplicacao(*numero_multiplicado))

print('-' * 20)

def impar_par(*args):
    total = 0
    
    for numero in args:
        total += numero
        if total % 2 == 0:
            print(f'Esse numero {numero} é um numero par.')
            continue
        else:
            print(f'Esse numero {numero} é um numero impar.')
            continue

impar_par(4,6,7,9)