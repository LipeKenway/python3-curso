# OPERADORES LOGICOS (OR)
#
# and (e)
# or (ou)
# not (nao)
#
# or = Qualquer condição como verdadeira avalia
# toda a expressão como verdadeira.
# 
# Se qualquer valor for considerado verdadeiro, a expressão inteira
# sera avaliada naquele valor.
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

senha_digitada = input('Senha: ') or 'Sem Senha'

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
     print('Sair')


# Avaliação de curto circuito
# print(True and 0 and True)
# teste = 0.0 or False or 0 or 'abc' or True
# print(teste)

# senha = input('Senha: ') or 'Sem Senha'
# print(senha)
