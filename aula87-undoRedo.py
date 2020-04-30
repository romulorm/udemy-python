to_do = []
re_do = []

def listar_tarefas():
    print('== Lista de Tarefas: ==')
    for tarefa in to_do:
        print(f'\t- {tarefa}')


def adicionar_tarefa(task):
    to_do.append(task)


def desfazer(lst_todo, lst_redo):
    if not lst_todo:
        print('Nada a desfazer!')
        return

    last_todo = lst_todo.pop()
    lst_redo.append(last_todo)


def refazer(lst_todo, lst_redo):
    if not lst_redo:
        print('Nada a refazer!')
        return

    last_redo = lst_redo.pop()
    lst_todo.append(last_redo)


while True:
    todo = str(input('Insira uma tarefa ou as opções "undo", "redo", "ls" ou "sair": ').upper())
    if todo == 'LS':
        listar_tarefas()
    elif todo == 'UNDO':
        desfazer(to_do, re_do)
    elif todo == 'REDO':
        refazer(to_do, re_do)
    elif todo == 'SAIR':
        print('Programa finalizado!')
        exit(0)
    else:
        adicionar_tarefa(todo)
