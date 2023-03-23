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


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        print()
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
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


while True:
    print('Comandos: Listar, Desfazer e Refazer')
    tarefa = input('Digite uma tarefa ou comando: ').capitalize()

    if tarefa == 'Listar':
        listar(tarefas)
        continue

    elif tarefa == 'Desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'Refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'Clear':
        os.system('cls')
        continue

    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
