'''
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''

import itertools

def cabecalho(titulo):
    print('-=-' * 10)
    print(f'{titulo:^30}')
    print('-=-' * 10)

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

cabecalho('COMBINATIONS')
for grupo in itertools.combinations(pessoas, 2):
    print(grupo)

cabecalho('PERMUTATIONS')
for grupo in itertools.permutations(pessoas, 2):
    print(grupo)

cabecalho('PRODUCT')
for grupo in itertools.product(pessoas, repeat=2):
    print(grupo)


aposta = [2, 10, 18, 23, 25, 31, 35, 44, 56, 59]

cont = 0
cabecalho('MEGA-SENA')
for cartela in itertools.combinations(aposta, 6):
    print(cartela)
    cont += 1
print(f'Qtde de cartelas: {cont}')

