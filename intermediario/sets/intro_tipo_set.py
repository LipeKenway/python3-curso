"""
Sets -> Conjunto em Python (tipo set)

* Conjuntos são ensinados na matematica
* Representados graficamente pelo diagrama de Venn
* Sets em Python são mutaveis, porem aceitam apenas tipos imutaveis
  como valor interno.

Criando um set
* set(iteravel) ou {1, 2, 3}

# s1 = set() # vazio
# s2 = {'Felipe', 1, 2, 3} # com dados
# print(s1)
# print(s2)


Sets são eficientes para remover valores duplicados de iteraveis.


# l1 = [1, 2, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

* Eles não tem indexação;
* Eles não garantem ordem;
* Eles são iteraveis (for, in, not in).


# s1 = {1, 2, 3}
# print(3 not in s1)

# for numero in s1:
#     print(numero)


Metodos uteis:
* add;
* update;
* clear;
* discard;

# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.add('Felipe')
# s1.update(('Ola Mundo', 4, 5, 6))
# s1.clear()
# s1.discard('Ola Mundo')
# s1.discard('Felipe')
# print(s1)

Operadores Úteis
* União (|) União (union) -> Une
* Intersecção (&) (intersection) -> Itens presentes em ambos.
* Diferença (-) -> Itens presentes apenas no set da esquerda.
* Diferença Simetrica (^) -> Itens que não estão em ambos.

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# s3 = s1 | s2
# print(s3)
# s3 = s1 & s2
# print(s3)
# s3 = s1 - s2
# print(s3)
# s3 = s1 ^ s2
# print(s3)
"""


# Exemplo do uso dos sets

# letras = set()

# while True:
#     letra = input('Digite: ')
#     letras.add(letra.lower())

#     if 'l' in letras:
#         print('Achou :)')
#         break

#     print(letras)








