"""
# Funções recursivas e recursividade

! Funções que podem se chamar de volta.
! Úteis p/ dividir problemas grandes em partes menores.

# Toda função recursiva deve ter:

! -> Um problema que possa ser dividido em partes menores;
! -> Um caso recursivo que resolve o pequeno problema;
! -> Um caso base que vai parar a recursão;
! -> Fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120 
"""
# def recursiva(inicio=0, fim=4):
#     print(inicio, fim)
    
#     if inicio >= fim: # caso base
#         return fim
    
#     inicio += 1 # Caso Recursivo, contar até o final.
    
#     return recursiva(inicio, fim)

# print(recursiva())

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))