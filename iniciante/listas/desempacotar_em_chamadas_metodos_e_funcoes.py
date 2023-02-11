"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Felipe', 'Maria', 'Luiz', 'Carla', 'Ana', 'Eduardo']
tupla = 'Python', 'é', 'legal.'

# p, s, *_, ap, u = lista
# print(p, ap, u)

# print(*lista)
# print(*string)
# print(*tupla)

salas = [
        # 0
    ['Maria', 'Luiz'], # 0 | 1
    
        # 1
    ['Eduarda'], # 0 
    
        # 2
    ['Felipe', 'Carla'], # 0 | 1
    
        # 3
    ['Lucas', 'Fernando', 'João'], # 0 | 1 | 2
    
        # 4
    ['Claudio', 'Henrique', 'Ana', 'Matheus'] # 0 | 1 | 2 | 3
]


print(*salas, sep='\n')