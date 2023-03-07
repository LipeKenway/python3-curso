# from sys import path
# print(*path, sep='\n')

# from pacotes.intro_packages import *
# import pacotes.intro_packages
# from pacotes import intro_packages
# from pacotes.intro_packages import soma_do_modulo

# print(variavel)
# print(pacotes.intro_packages.soma_do_modulo(5, 5))
# print(intro_packages.soma_do_modulo(4, 7))
# print(soma_do_modulo(4, 2))

# from pacotes import falar_oi, soma_do_modulo
# a linha acima vai funcionar fora da pasta pacotes dentro de intermediario

from modulo_1 import soma_do_modulo, variavel, nova_variavel
from modulo_2 import falar_oi

falar_oi()
print(soma_do_modulo(3, 4))
print(variavel)
print(nova_variavel)


