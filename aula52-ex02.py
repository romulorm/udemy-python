'''
Crie uma função mestre que possa receber outras duas funções como parâmetros que recebem um número diferente de argumentos.
'''


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi, {nome}.'


def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}. Tudo bem contigo?'


# PROGRAMA PRINCIPAL

exec1 = mestre(saudacao, 'Bom dia', 'Luiz')
exec2 = mestre(fala_oi, 'Luiz')
print(exec1)
print(exec2)
