"""
! Entendendo os seus proprios módulos Python

* O Primeiro modulo executado chama-se __main__
* Voce pode importar outro módulo inteiro ou parte do modulo.

* O Python conhece a pasta onde o __main__ esta 
* e as pastas abaixo dele

* Ele não reconhece pastas e modulos acima do __main__ por padrão.

* O Python conhece todos os modulos e pacotes presentes 
* nos caminhos de sys.path
"""
import arq_aula_modularizacao
from arq_aula_modularizacao import soma, variavel_modulo

# print('Este modulo se chama', __name__)
print(variavel_modulo)
print(soma(2, 3))
print(arq_aula_modularizacao.soma(3, 3))