"""
# Class -> Classes são moldes para criar novos objetos.

# As classes geram novos objetos (instancias) que podem
# ter seus proprios atributos e metodos.

# Os objetos gerados pela classe podem usar seus dados internos
# para realizar varias ações.

# Por convenção, usamos PascalCase para nomes de classes.
"""
# string = 'Felipe'  # str

# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Felipe', 'Soares')
# p1.nome = 'Felipe'
# p1.sobrenome = 'Soares'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
