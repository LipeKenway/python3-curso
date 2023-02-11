"""
# Conversão de Tipos (Coerção)

* type convertion, typecasting, coercion
* é o ato de converter um tipo em outro
* tipos imutaveis e primitivos: str, int, float, bool
"""

print(1 + 1)
print('a' + 'b')

print('-' * 20)

print(int('2'), type(int('2'))) # Verificando o tipo da variavel
print(int('2') + 2) # Convertendo str para int

print('-' * 20)

print(float(1), type(float(1))) # Verificando o tipo da variavel
print(float(1) + 2) # Convertendo um numero int para um numero float

print('-' * 20)

print(bool(' '), type(bool(' '))) # Verificando o tipo da variavel
print(bool(' ')) # Convertendo para um tipo bool