"""
Try, Except, Else e Finally
"""
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0    
    # print(b[0])
    print('linha 1'[1000])
    c = a / b


except ZeroDivisionError:
    print('Não eh possivel dividir por zero.')
    
except NameError:
    print('Alguns dos campos não foi preenchido.')

except (TypeError, IndexError) as error:
    print('Type Error + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)

except Exception:
    print('Erro Desconhecido.')

print('Continuar...')