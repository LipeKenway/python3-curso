"""
# Decoradores com parametros
"""
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')
            
        def aninhada(*args, **kwargs):
            print('Parametros do decorador: ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

soma_conta = soma(10, 5)
multiplicacao_conta = multiplica(10, 5)

print(soma_conta)
print(multiplicacao_conta)