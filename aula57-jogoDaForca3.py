'''
Jogo da advinhação de palavras aprimorado com dicionários de temas contendo as palavras.
Atualização 3: Adicionadas as dicas com a utilização de dicionários.
'''

from random import randint
from time import sleep

opcoes = ('1) Animais', '2) Corpo Humano', '3) Comida', '4) >> SAIR DO JOGO <<')

animais = {
    0: {'nome': 'zebra', 'caracteristicas': 'Possui listras pretas.'},
    1: {'nome': 'elefante', 'caracteristicas': 'Bem pesado.'},
    2: {'nome': 'lagosta', 'caracteristicas': 'Muito cara.'},
    3: {'nome': 'leao', 'caracteristicas': 'Possui juba.'},
    4: {'nome': 'cobra', 'caracteristicas': 'Rasteja no chão.'},
    5: {'nome': 'escorpiao', 'caracteristicas': 'Possui um ferrão na cauda.'},
    6: {'nome': 'abelha', 'caracteristicas': 'Produz mel.'},
    7: {'nome': 'girafa', 'caracteristicas': 'Possui um enorme pescoço.'},
    8: {'nome': 'macaco', 'caracteristicas': 'Aprecia uma banana.'},
    9: {'nome': 'morcego', 'caracteristicas': 'Voa e possui hábitos noturnos.'},
    10: {'nome': 'esquilo', 'caracteristicas': 'Adora uma noz'},
    11: {'nome': 'enguia', 'caracteristicas': 'Algumas são elétricas'},
    12: {'nome': 'urubu', 'caracteristicas': 'Não pode ver algo apodrecendo que já se aproxima.'}
}

corpoHumano = {
    0: {'nome': 'braco', 'caracteristicas': 'Geralmente é o local onde se toma vacina.'},
    1: {'nome': 'perna', 'caracteristicas': 'Característica X'},
    2: {'nome': 'cabeca', 'caracteristicas': 'Característica X'},
    3: {'nome': 'olho', 'caracteristicas': 'Característica X'},
    4: {'nome': 'dente', 'caracteristicas': 'Característica X'},
    5: {'nome': 'lingua', 'caracteristicas': 'Característica X'},
    6: {'nome': 'unha', 'caracteristicas': 'Característica X'},
    7: {'nome': 'cabelo', 'caracteristicas': 'Característica X'},
    8: {'nome': 'coracao', 'caracteristicas': 'Característica X'},
    9: {'nome': 'pulmao', 'caracteristicas': 'Característica X'},
    10: {'nome': 'figado', 'caracteristicas': 'Característica X'},
    11: {'nome': 'estomago', 'caracteristicas': 'Característica X'},
    12: {'nome': 'intestino', 'caracteristicas': 'Característica X'}
}

comida = {
    0: {'nome': 'macarrao', 'caracteristicas': 'É duro quando cru e mole quando cozido.'},
    1: {'nome': 'arroz', 'caracteristicas': 'Característica X'},
    2: {'nome': 'pizza', 'caracteristicas': 'Característica X'},
    3: {'nome': 'sanduiche', 'caracteristicas': 'Característica X'},
    4: {'nome': 'lasanha', 'caracteristicas': 'Característica X'},
    5: {'nome': 'almondega', 'caracteristicas': 'Característica X'},
    6: {'nome': 'salada', 'caracteristicas': 'Característica X'},
    7: {'nome': 'frango', 'caracteristicas': 'Característica X'},
    8: {'nome': 'tomate', 'caracteristicas': 'Característica X'},
    9: {'nome': 'farinha', 'caracteristicas': 'Característica X'},
    10: {'nome': 'batata', 'caracteristicas': 'Característica X'},
    11: {'nome': 'couve', 'caracteristicas': 'Característica X'}
}

nome_cat = ''
digitadas = list()

while True:
    print('-=-' * 6)
    print('\33[36mJOGO DA FORCA 3.0\33[m')
    print('-=-' * 6)
    print('\33[35mCategorias disponíveis:\33[m')
    chances = 5
    tentativas = 0
    for opc in opcoes:
        print(opc)
    opcao = input('\33[34mSua opção: \33[m').strip()[0]
    while opcao not in '1234':
        print('Opção inválida!')
        opcao = (input('\33[34mSua opção: \33[m'))
    if opcao == '1':
        nome_cat = 'animais'
        palavra_secreta = animais[randint(0, len(animais) - 1)]['nome']
        for v in animais.values():
            if palavra_secreta in v['nome']:
                dica = (v['caracteristicas'])
    if opcao == '2':
        nome_cat = 'corpo humano'
        palavra_secreta = corpoHumano[randint(0, len(corpoHumano) - 1)]['nome']
        for v in corpoHumano.values():
            if palavra_secreta in v['nome']:
                dica = (v['caracteristicas'])
    if opcao == '3':
        nome_cat = 'comida'
        palavra_secreta = comida[randint(0, len(comida) - 1)]['nome']
        for v in comida.values():
            if palavra_secreta in v['nome']:
                dica = (v['caracteristicas'])
    if opcao == '4':
        print('\33[31mObrigado por ter jogado. Volte sempre!\33[m')
        exit(0)

    while True:
        letra = str(input(f'Escolha uma letra para a categoria \33[35m{nome_cat}\33[m: ').strip().lower()[0])
        digitadas.append(letra)
        if letra in palavra_secreta:
            print('Você acertou uma letra da palavra!')
        else:
            print('Não foi dessa vez. Continue tentando até esgotar suas chances.')
            tentativas += 1
            chances -= 1
            digitadas.pop()
            print(f'\33[31mChances remanescentes: {chances}\33[m')
            if chances == 2:
                print(f'\033[1;30;44mDica: {dica}\33[m')
            if chances == 0:
                print('-' * 20)
                print('\33[31mFim da partida. Você esgotou suas chances.\33[m')
                print()
                break
        palavra_temporaria = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in digitadas:
                palavra_temporaria += letra_secreta
            else:
                palavra_temporaria += '*'
        if palavra_temporaria == palavra_secreta:
            print(f'\33[36mParabéns, você advinhou. A palavra secreta era \33[34m{palavra_secreta}\33[m.')
            print(f'Número de tentativas erradas: \33[31m{tentativas}\33[m')
            print()
            print()
            print()
            digitadas = []
            sleep(3)
            break
        else:
            print(f'A palavra secreta está assim: \33[34m{palavra_temporaria}\33[m')
