'''
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função 2 executada.
'''
from datetime import datetime

def periodo():
    h = datetime.now().hour
    if 0 <= h <= 11:
        return 'Bom dia'
    elif 12 <= h <= 17:
        return 'Boa tarde'
    else:
        return 'Boa noite'


def saudacao(funcao, nome):
    print(f'{funcao()}, {nome}. Tudo bem contigo?')


# PROGRAMA PRINCIPAL

name = str(input('Digite o seu nome: '))
saudacao(periodo, name)
