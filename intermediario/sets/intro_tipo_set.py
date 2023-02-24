"""
Sets -> Conjunto em Python (tipo set)

* Conjuntos são ensinados na matematica
* Representados graficamente pelo diagrama de Venn
* Sets em Python são mutaveis, porem aceitam apenas tipos imutaveis
  como valor interno.

Criando um set
* set(iteravel) ou {1, 2, 3}


Sets são eficientes para remover valores duplicados de iteraveis.

* Eles não tem indexação;
* Eles não garantem ordem;
* Eles são iteraveis (for, in, not in).


Metodos uteis:
* add;
* update;
* clear;
* discard;
"""



s1 = set() # vazio
s2 = {'Felipe', 1, 2, 3} # com dados
print(s1)
print(s2)