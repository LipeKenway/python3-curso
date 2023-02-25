"""
Exercicio

* Crie uma função que encontra o primeiro duplicado considerando 
  o segundo numero como a duplicação. Retorne a duplicação considerada.

Requesitos:
* A ordem do numero duplicado é considerada a partir da segunda
ocorrencia do numero, ou seja o numero duplicado em si.

Exemplo:
* [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3).
* [1, 2, 3, 4, 5, 6] -> Retorne 1 (não tem duplicados).
* Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [8, 6, 1, 4, 4, 2, 5, 9],
    [9, 4, 5, 10, 5, 3, 10, 6],
    [6, 7, 7, 6, 10, 6, 8, 1],
    [4, 9, 8, 4, 2, 5, 2, 7],
    [5, 8, 2, 7, 3, 9, 1, 3],
    [1, 6, 4, 10, 9, 10, 5],
    [1, 4, 3, 5, 2, 9, 10, 7],
    [7, 2, 6, 2, 5, 8, 7, 10],
    [10, 9, 3, 4, 7, 1, 8, 5, 8],
    [2, 9, 10, 3, 5, 7, 6, 3, 8],
    [3, 10, 5, 2, 4, 9, 8, 4, 1],
]

def encontrar_duplicados(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
            
        numeros_checados.add(numero)

    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(f'{lista} -> O Nº repetido eh {encontrar_duplicados(lista)}.')