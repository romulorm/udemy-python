'''
Jogo da advinhação de palavras simples.
Chances: 5
'''

palavra_secreta = 'macaco'
digitadas = []
chances = 5
tentativas = 0

print('-=-' * 6)
print('\33[36mJOGO DA FORCA 1.0\33[m')
print('-=-' * 6)

while True:
    letra = str(input('Escolha uma letra: ').strip().lower()[0])
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
        print(f'Parabéns, você acertou. A palavra secreta era \33[34m{palavra_secreta}\33[m.')
        print(f'Número de tentativas erradas: {tentativas}')
        break
    else:
        print(f'A palavra secreta está assim: \33[33m{palavra_temporaria}\33[m')


