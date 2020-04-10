'''
Iteração de Strings com While
Faça um exercício que revele a letra que mais apareceu no texto, desconsiderando os espaços.
'''

while True:
    conta_letra = letra_maior = ''
    letra_qtde = 0

    frase = str(input('Digite uma frase (fim para sair): ').upper())
    if frase == 'FIM':
        break
    for letra in frase:
        conta_letra = frase.count(letra)
        if conta_letra > letra_qtde and frase.strip():
            letra_qtde = conta_letra
            letra_maior = letra
    print(f'A letra \33[32m{letra_maior}\33[m apareceu mais vezes no texto: \33[32m{letra_qtde}\33[m vezes.')
