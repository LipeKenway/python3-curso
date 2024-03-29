"""
# Execicio -> Lista de tarefas com desfazer e refazer

tarefas = [] -> lista de tarefas
tarefas = ['Limpar a Casa'] -> Adicionei uma tarefa
tarefas = ['Limpar a Casa', 'Caminhar'] -> Adicionei Caminhar

desfazer = ['Limpar a Casa',] -> Refazer ['Caminhar']
desfazer = [] -> Refazer ['Limpar a Casa', 'Caminhar']

refazer = tarefas['Limpar a Casa']
refazer = tarefas['Limpar a Casa', 'Caminhar']
"""
import os
import json
from time import sleep

caminho_arquivo = r'C:\\Users\\lyppy\\Downloads\\Cursos\\python\\intermediario\\exercicios\\'
caminho_arquivo += 'lista_de_tarefas.json'


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados

    except FileNotFoundError:
        print('Arquivo JSON ainda não existe.')
        print()
        salvar(tarefas, caminho_arquivo)
        print('Criando, arquivo JSON...')
        print()
        sleep(2)
    return dados


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Voce nao digitou uma tarefa.')
        return

    print(f'"{tarefa}" adicionada a lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)
    print()


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        print()
        return

    print('Tarefas:')
    for index, tarefa in enumerate(tarefas):
        print(f'\t{index+1}) {tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        print()
        return

    tarefa = tarefas.pop()
    print(f'"{tarefa}" removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        print()
        return

    tarefa = tarefas_refazer.pop()
    print(f'"{tarefa}" retornou a lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)
    print()


tarefas = ler([], caminho_arquivo)
tarefas_refazer = []


while True:
    print('Comandos: Listar, Desfazer e Refazer')
    tarefa = input('Digite uma tarefa ou comando: ').capitalize()

    comandos = {
        'Listar': lambda: listar(tarefas),
        'Desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'Refazer': lambda: refazer(tarefas, tarefas_refazer),
        'Clear': lambda: os.system('cls'),
        'Adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(
        tarefa) is not None else comandos['Adicionar']

    comando()
    salvar(tarefas, caminho_arquivo)
