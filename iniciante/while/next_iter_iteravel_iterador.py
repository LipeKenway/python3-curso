"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega o iterador
"""

texto = 'Felipe' # Iteravel
iterador = iter(texto) # Iterador

# for letra in texto:
#   print(letra)

while True:
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
        break