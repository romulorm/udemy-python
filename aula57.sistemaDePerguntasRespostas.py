print('-=-' * 6)
print('\33[36mJOGO DA MATEMÁTICA\33[m')
print('-=-' * 6)

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'alternativas': {'a': '3', 'b': '4', 'c': '5', 'd': '1'},
        'resposta_certa': 'b'
        },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2?',
        'alternativas': {'a': '3', 'b': '4', 'c': '5', 'd': '6'},
        'resposta_certa': 'd'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 4+3?',
        'alternativas': {'a': '3', 'b': '4', 'c': '7', 'd': '8'},
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 2-2?',
        'alternativas': {'a': '3', 'b': '4', 'c': '0', 'd': '1'},
        'resposta_certa': 'c'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 3*3?',
        'alternativas': {'a': '9', 'b': '6', 'c': '5', 'd': '1'},
        'resposta_certa': 'a'
    },
}
resp_certas = 0
porcentagem = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for ak, av in pv['alternativas'].items():
        print(f'[{ak}]: {av}')
    resposta = str(input('Letra da sua resposta: ').lower().strip()[0])
    if resposta == pv['resposta_certa']:
        print('\33[32mUeebaaa, você acertou!\33[m')
        resp_certas += 1
    else:
        print('\33[31mQue pena! Você errou!\33[m')
    print('-=-' * 20)
qtde_perguntas = len(perguntas)
porcentagem = resp_certas / qtde_perguntas * 100
print(f'Quantidade de respostas certas: \33[32m{resp_certas}\33[m')
print(f'Porcentagem de acertos: \33[34m{porcentagem}%\33[m')
