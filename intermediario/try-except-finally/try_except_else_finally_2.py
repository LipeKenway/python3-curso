"""
Try, Except, Else e Finally (Parte 2)
"""
try:
    print('Abrir arquivo.')
    # 8/0

except ZeroDivisionError as err:
    print(err.__class__.__name__)
    print(err)
    print('Não eh possivel dividir por zero.')

except NameError as err:
    print(err)
    print('Erro ao declarar a variavel.')

except (IndexError, TypeError):
    print('Index Error | TypeError.')

else:
    print('Não deu erro :)')

finally:
    print('Fechar arquivo.')