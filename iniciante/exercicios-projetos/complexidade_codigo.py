"""
CONSTANTE = "Variaveis" que não vão mudar

* Muitas condições no mesmo if (ruim)
* Contagem de complexidade (ruim)
"""

velocidade = 61 # Vel. Atual do carro
local_carro = 98 # local onde o carro esta na estrada

RADAR_1 = 60 # Vel. Maxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_radar_1 = velocidade > RADAR_1

local_2 = (LOCAL_1 - RADAR_RANGE)
local_3 = (LOCAL_1 + RADAR_RANGE)

local_radar_range = local_carro >= local_2 and local_carro <= local_3

carro_pass_radar_1 = local_radar_range and vel_carro_radar_1
                            
carro_multado_radar_1 = carro_pass_radar_1 and vel_carro_radar_1

if local_radar_range:    
    if vel_carro_radar_1:
        print('Veiculo ultrapassou o limite de velocidade do radar 1')
        print('-' * 50)

        if carro_multado_radar_1:
            print('Veiculo multado no radar 1')

    else:
        print('Dentro do Limite de velocidade do radar 1')

else:
    print('Nenhum veiculo passou no radar 1')
