from itertools import groupby

lst_alunos = [
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Leila', 'nota': 'C'},
    {'nome': 'Rodrigo', 'nota': 'B'},
    {'nome': 'Mário', 'nota': 'C'},
    {'nome': 'Karina', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Marisa', 'nota': 'B'},
    {'nome': 'Rubens', 'nota': 'C'},
    {'nome': 'Jairo', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'D'}
]

chave = lambda item: item['nota']
lst_alunos.sort(key=chave) # O groupby necessita da lista ordenada para funcionar
alunos_agrupados = groupby(lst_alunos, chave)

for notas, alunos_iteraveis in alunos_agrupados:
    print(f'\33[32mAlunos com nota {notas}:\33[m')
    for alunos in alunos_iteraveis:
        print(alunos['nome'])
