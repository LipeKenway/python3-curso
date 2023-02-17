"""
args -> Argumentos não nomeados

*args (Empacotamento e Desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1 = soma(95, 28, 23)
print('Total = ', soma_1)

soma_2 = soma(49, 54, 62)
print('Total = ', soma_2)

numeros = 47, 88, 29, 12, 10
soma_3 = soma(*numeros)
print('Total = ', soma_3)

print(sum(numeros))
