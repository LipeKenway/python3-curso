"""
Argumentos Nomeados e Não Nomeados em funções Python.

Argumentos Nomeados tem nome com sinal de igual.
Argumentos Não Nomeados recebe apenas o argumento (valor).
"""

# Definição -> (def)
def soma(x, y, z): # <- Parametros
    print(f'{x = } {y = } {z = }', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3) # <- Argumentos

# se um argumento for nomeado aqui os outros depois dele tbm serão.
soma(1, y=2, z=5) 
soma(y=2, z=3, x=1)
