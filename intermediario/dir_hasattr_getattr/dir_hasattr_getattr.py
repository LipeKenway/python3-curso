"""
dir, hasattr e getattr em Python
"""
string = 'Felipe'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe')
    print(getattr(string, metodo)())
else:
    print('Não existe esse metodo', metodo)