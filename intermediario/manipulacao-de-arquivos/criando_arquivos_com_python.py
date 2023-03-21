"""
# Criando arquivos com Python 3

# Usamos a função open para abrir 
# um arquivo Python (ele pode ou não existir).

# Modos: 
    ! r -> (leitura), 
    ! w -> (escrita),
    ! x -> (para criação),
    ! a -> (escreve ao final),
    ! b -> (binario),
    ! t -> (modo texto),
    ! + -> (leitura e escrita).

# Context Manager -> with (abre e fecha).

# Metodos Uteis:
    ! write, read -> (escrever e ler),
    ! writelines -> (escrever varias linhas),
    ! seek (mover o cursor),
    ! readline -> (ler linha),
    ! readlines -> (ler linhas).

# Vamos falar mais sobre o modulo os, mas:
    ! os.remove ou unline -> (apaga o arquivo),
    ! os.rename -> (troca o nome ou move o arquivo).

# Vamos falar mais sobre o modulo JSON, mas:
    ! json.dump -> (gera um arquivo .json),
    ! json.load ->
"""
caminho_arquivo = 'C:\\Users\\lyppy\\Downloads\\Cursos\\python\\intermediario\\manipulacao-de-arquivos\\'
caminho_arquivo += 'aula_teste.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá Mundo')
    print('O arquivo vai ser fechado.')
