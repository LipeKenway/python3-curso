"""
Recarregando Modulos, importlib e Singleton
"""
import importlib

import arq_aula_recarregando_modulos

print(arq_aula_recarregando_modulos.variavel)

for i in range(10):
    importlib.reload(arq_aula_recarregando_modulos)
    print(i)
    
print('Fim')