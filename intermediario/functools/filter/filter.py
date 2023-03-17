"""
# Filter -> eh um filtro funcional
"""
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
def filtrar_preco(produto):
    return produto['preco'] >= 20
    
produtos = [
    {'nome': 'Produto 4', 'preco': 10.90},
    {'nome': 'Produto 1', 'preco': 50.20},
    {'nome': 'Produto 5', 'preco': 26.11},
    {'nome': 'Produto 3', 'preco': 75.40},
    {'nome': 'Produto 2', 'preco': 15.24},
]

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 20
# ]

novos_produtos = filter(
    # lambda p: p['preco'] >= 20
    filtrar_preco, 
    produtos)

print_iter(produtos)
print_iter(novos_produtos)