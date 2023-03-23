"""
# Controlando a quantidade de argumentos posicionais e nomeados
  em funções
  
-> *args (ilimitado de argumentos posicionais);
-> **kwargs (ilimitado de argumentos nomeados)

# Positional-Only Parameters (/) 
    ! -> Tudo antes da barra deve ser "apenas" posicional.
# Keyword-Only Arguments (*)
    ! -> Tudo depois do asterisco deve ser nomeado na chamada da função.
"""


def soma(a, b, /, x, y):
    print(a + b + x + y)


def sub(a, b, /, x, *, y, z):
    print(a - b - x - y - z)


soma(8, 8, 6, y=3)
sub(60, 8, 6, y=3, z=8)
