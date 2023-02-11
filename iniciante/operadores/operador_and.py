# OPERADORES LOGICOS (AND)
#
# and (e)
# or (ou)
# not (nao)
#
# and = Todas as condições precisam ser verdadeiras.
#
# Se qualquer valor for considerado falso, a expressao inteira 
# será avaliada naquele valor. 
#
# São considerados falsos (que eu ja vi):
# 
# 0
# 0.0
# ''
# False
#
# Tambem existe o tipo (None) 
# que é usado para representar um 'não valor'.

entrada = input('[E]ntrar [S]air: ')

senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
     print('Sair')


# Avaliação de curto circuito
# print(True and True and True)
# print(True and False and True)
# print(True and 0 and True)


