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
* extend(); -> Estende a lista + Concatenar listas.

Create | Read | Update  | Delete
Criar  | Ler  | Alterar | Apagar = lista[i] (CRUD)

"""
#        0 | 1 | 2 | 3 
lista = [10, 20, 30, 40]

lista.append('Felipe')
nome = lista.pop()
print(lista)

# print(lista, nome)

lista.append(1233)
del lista[-1] # -1 Sempre eh o ultimo item da lista
print(lista)

lista.insert(0, 0)
print(lista)








