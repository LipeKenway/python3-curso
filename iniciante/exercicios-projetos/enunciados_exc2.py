"""
* Faça um programa que pergunte a hora ao usuario; 
* Baseando-se no horario descrito, exiba a saudação apropriada. 

EX.: Bom dia 0-11;
     Boa tarde 12-17; 
     Boa noite 18-23.
"""

entrada = input('Digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)

    bom_dia = hora >= 0 and hora <= 11
    boa_tarde = hora >= 12 and hora <= 17
    boa_noite = hora >= 18 and hora <= 23

    if bom_dia:
        print('Bom Dia :)')

    elif boa_tarde:
        print('Boa Tarde :)')

    elif boa_noite:
        print('Boa Noite :)')
    
    else:
        print('Desculpe, isso não eh um horario valido.')

except:
    print('Por favor, digite apenas numeros inteiros.')

