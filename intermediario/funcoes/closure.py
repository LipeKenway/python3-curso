"""
Closure e funções que retornam outras funções.
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom Dia')
falar_boa_tarde = criar_saudacao('Boa Tarde')
falar_boa_noite = criar_saudacao('Boa Noite')

for nome in ['Maria', 'Felipe']:
    print(falar_bom_dia(nome))
    print('-' * 50)
    print(falar_boa_tarde(nome))
    print('-' * 50)
    print(falar_boa_noite(nome))
    print('-' * 50)
