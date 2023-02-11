"""
Repetições

while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
"""

contador = 0

while contador < 50:

    contador += 1

    if contador == 6:
        print('Não vou mostar o', contador)
        continue

    if contador >= 10 and contador <= 30:
        print('Não vou mostra o', contador)
        continue

    print(contador)

    if contador == 40:
        break
    
print('Acabou')