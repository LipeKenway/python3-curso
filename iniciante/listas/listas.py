"""
Listas em Python

Tipo list -> Mutavel
Suporta varios valores de qualquer tipo

Conhecimentos reutilizaveis -> indices e fatiamento

Metodos Uteis: 
* append(); 
* insert(); 
* pop(); 
* del(); 
* clear(); 
* extend();

etc...
"""

# ........01234 -> Posição Positiva
# .......-54321 <- Posição Negativa
string = 'ABCDE' # 5 Caracteres len()

# Uma lista vazia eh igual ah um boolean False.
# print(bool([]))

lista = [123, True, 'Felipe Soares', 1.2, []]

# Na lista eh possivel troca os valores

lista[-3] = 'Maria'

print(lista)

print(lista[2], type(lista[2]))





