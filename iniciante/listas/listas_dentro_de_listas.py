"""
Listas de listas e seus indices
"""

salas = [
        # 0
    ['Maria', 'Luiz'], # 0 | 1
    
        # 1
    ['Eduarda', (0, 10, 20, 30, 40)], # 0 | (1) -> 0 | 1 | 2 | 3 | 4
    
        # 2
    ['Felipe', 'Carla'], # 0 | 1
    
        # 3
    ['Lucas', 'Fernando', 'João'], # 0 | 1 | 2
    
        # 4
    ['Claudio', 'Henrique', 'Ana', 'Matheus'] # 0 | 1 | 2 | 3
]

# print(salas[3][2])
# print(salas[2][0])
# print(salas[4][2])
# print(salas[1][1][2])

print('-' * 50)

for sala in salas:
    print(f'A sala eh {sala}')
    print('-' * 50)

    for aluno in sala:
        print(aluno)
        


