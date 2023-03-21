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
import os

caminho_arquivo = r'C:\\Users\\lyppy\\Downloads\\Cursos\\python\\intermediario\\manipulacao-de-arquivos\\'
os.chdir(caminho_arquivo)
caminho_arquivo += 'aula_teste.txt'


# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    print('ESCREVENDO')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3 \n', 'Linha 4\n'))
    arquivo.seek(0, 0)
    print(arquivo.read())

    print('=' * 20)

    print('LENDO')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('=' * 20)

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('=' * 20)

# os.rename(caminho_arquivo, 'aula_teste.txt')
# os.unlink(caminho_arquivo)
