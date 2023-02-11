"""
Exercicio

CPF: 746.824.890-70

Colete a soma dos 9 primeiros digitos do CPF multiplicando 
cada um dos valores por uma contagem regressiva começando de 10.

Ex.: 746.824.890-70 (746824890)
  10  9   8   7   6   5   4   3   2
* 7   4   6   8   2   4   8   9   0
  70  36  48  56  12  20  32  27  0

Somar todos os resultados:
-> 70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado anterior por 10: 
-> 301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11:
-> 3010 % 11 = 7

Se o Resultado anterior for maior que 9:
-> Resultado é 0

Contrario disso:
-> Resultado é o valor da conta

O Primeiro digito do CPF é -> 7.
"""
import re
import sys

entrada = input('CPF [746.824.890-70]: ')
cpf_usuario =re.sub(
  r'[^0-9]', 
  '', 
  entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
  print('Voce enviou dados sequenciais.')
  sys.exit()

digitos_formatados = cpf_usuario[:9] # Tirando os 2 ultimos digitos.

# Converter uma string para uma lista de inteiros
lista_numeros_cpf = [int(n) for n in digitos_formatados] 

resultado_digito_1 = 0
contador_regressivo_1 = 10

# Primeiro digito do CPF
for digito in digitos_formatados:
  resultado_digito_1 += int(digito) * contador_regressivo_1
  contador_regressivo_1 -= 1

# Multiplicando e pegando o resto da soma de todos os digitos.
digito_1 = (resultado_digito_1 * 10) % 11

# Se o digito for maior que 9 o digito vira 0.
digito_1 = digito_1 if digito_1 <= 9 else 0

# Inserindo o primeiro digito na lista.
lista_numeros_cpf.append(digito_1) 

resultado_digito_2 = 0
contador_regressivo_2 = 11

# Segundo digito do CPF.
for digito in lista_numeros_cpf:
  resultado_digito_2 += int(digito) * contador_regressivo_2
  contador_regressivo_2 -= 1

# Multiplicando e pegando o resto da soma de todos os digitos.
digito_2 = (resultado_digito_2 * 10) % 11

# Se o digito for maior que 9 o digito vira 0.
digito_2 = digito_2 if digito_2 <= 9 else 0

# Inserindo o segundo digito na lista.
lista_numeros_cpf.append(digito_2) 

# Add devolta o os pontos.
lista_numeros_cpf.insert(3, '.') 
lista_numeros_cpf.insert(7, '.')

# Add devolta o traço.
lista_numeros_cpf.insert(11, '-')

cpf_gerado = f'{digitos_formatados}{digito_1}{digito_2}'

if cpf_usuario == cpf_gerado:
  print(f'O CPF {cpf_usuario} é Valido.')

else:
  print(f'O CPF {cpf_usuario} esta Invalido')


"""
cpf = '74682489070'
novo_digito = cpf[:9]

resultado = 0
contador_regressivo = 10

for digito in novo_digito:
  resultado += int(digito) * contador_regressivo
  contador_regressivo -= 1

digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0

print(digito)




cpf_usuario ='746.824.890-70' \
  .replace(' ', '') \
  .replace('.', '') \
  .replace('-', '') # Removendo os pontos, traços e espaços.


for digito in lista_numeros_cpf:
  print(f'{digito}', end='') 

print('\n')

"""


