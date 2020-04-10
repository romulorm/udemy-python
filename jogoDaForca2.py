'''
Jogo da advinhação de palavras aprimorado com dicionários de temas contendo as palavras.
Chances: 5
'''

from random import randint

animal = ('zebra', 'elefante', 'leao', 'cobra', 'escorpiao', 'abelha', 'girafa', 'galinha', 'macaco', 'morcego',
          'esquilo', 'enguia', 'urubu', 'lagosta')
corpoHumano = ('braco', 'perna', 'cabeca', 'olho', 'orelha', 'dente', 'lingua', 'unha', 'cabelo', 'coracao',
               'pulmao', 'figado', 'estomago', 'intestino', 'pancreas')
comida = ('macarrao', 'arroz', 'pizza', 'sanduiche', 'lasanha', 'almondega', 'salada', 'frango', 'tomate',
          'farinha', 'batata', 'abobora', 'couve', 'cenoura')

palavra_secreta = ''
digitadas = []
chances = 5
tentativas = 0

cat = input('Escolha o tema: \33[33m1\33[m-Animal, \33[33m2\33[m-Corpo Humano, \33[33m3\33[m-Comida: ')
while True:
    if cat not in '123':
        print('Digite o número de uma categoria válida.')
        cat = input('Escolha uma categoria: 1-Animal, 2-Corpo Humano, 3-Comida: ')
    else:
        if cat == '1':
            palavra_secreta = animal[randint(0, len(animal))]
            nome_cat = 'Animal'
            break
        elif cat == '2':
            palavra_secreta = corpoHumano[randint(0, len(corpoHumano))]
            nome_cat = 'Corpo Humano'
            break
        elif cat == '3':
            palavra_secreta = comida[randint(0, len(comida))]
            nome_cat = 'Comida'
            break
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
        print(f'Chances remanescentes: {chances}')
        if chances == 0:
            print('\33[31mFim da partida. Você esgotou suas chances.\33[m')
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
        break
    else:
        print(f'A palavra secreta está assim: \33[34m{palavra_temporaria}\33[m')
