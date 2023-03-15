l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def unir_lista(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

print(unir_lista(l1, l2))