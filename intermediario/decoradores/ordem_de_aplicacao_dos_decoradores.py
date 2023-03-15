"""
# Ordem de aplicação dos decoradores
"""
def parametros_decorador(nome):
    def decorador(func):
        print('Decoradora:', nome)
            
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y

soma_conta = soma(10, 5)
print(soma_conta)
