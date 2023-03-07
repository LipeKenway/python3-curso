"""
Modulos padrão do Python (import, from, as e *)

* inteiro -> import (nome do modulo)
* Vantagens: Vc tem o namespace do modulo.
* Desvantagens: Nomes grandes.

* partes -> from (nome do modulo) import (objeto 1, objeto 2)
* Vantagens: Nomes pequenos.
* Desvantagens: Sem o namespace do modulo.

* alias 1 -> import (nome do modulo) as (apelido)
* alias 2 -> from (nome do modulo) import (objeto) as (apelido)
* Vantagens: Vc pode reservar nomes para seu codigo.
* Desvantagens: Pode ficar fora do padrão da linguagem.

* Má pratica -> from (nome do modulo) import (*)
* Vantagens: Importa tudo de um modulo.
* Desvantagens: Importa tudo de um modulo.
"""
from sys import exit, platform

