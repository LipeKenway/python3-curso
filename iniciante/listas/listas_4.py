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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_c)
print(lista_a)






