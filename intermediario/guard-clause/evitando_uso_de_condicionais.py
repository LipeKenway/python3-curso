"""
# Guard Clause
"""
import os

tarefas = []
tarefas_refazer = []


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
