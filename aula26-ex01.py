'''
Faça um programa que peça ao usuário digitar um número inteiro. Informe se esse número é par ou ímpar. Caso o usuário
não digite um número inteiro, informe que não é um número inteiro.
'''

num = str(input('Digite um número inteiro: '))
try:
    if int(num) % 2 == 0:
        print('O número digitado é par!')
    else:
        print('O número digitado é ímpar!')
except:
    print('O valor digitado não é um número inteiro.')