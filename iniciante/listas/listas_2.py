"""
Listas em Python

Tipo list -> Mutavel
Suporta varios valores de qualquer tipo

Conhecimentos reutilizaveis -> indices e fatiamento

Metodos Uteis: 
* append(); -> Adiciona um item no final da lista.
* insert(); -> Adiciona um item no indice escolhido.
* pop(); -> Remove do final ou do indice escolhido.
* del(); -> Apaga um indice.
* clear(); -> Limpa a lista.
* extend(); -> Estende a lista.

Create | Read | Update  | Delete
Criar  | Ler  | Alterar | Apagar = lista[i] (CRUD)

"""
#        0 | 1 | 2 | 3 | 4 | 5 | 6
lista = [10, 20, 30, 40]
lista[2] = 300

print(lista[2])
del lista[2]

numero = lista[2]
print(numero)

lista.append(50)
lista.pop()

lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(2)

print(lista, 'O item removido foi ->', ultimo_valor)







