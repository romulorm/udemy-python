'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver até 4 letras, escreva: Seu nome é curto. Se tiver
5 a 8 letras, "Seu nome é normal", e acima de 8 letras, "Seu nome é muito grande".
'''

name = str(input('Qual é o seu nome? '))
separaNome = name.split(' ')
primeiroNome = separaNome[0]
if len(primeiroNome) <= 4:
    print(f'Olá {name}, o seu primeiro nome é curto.')
elif len(primeiroNome) > 8:
    print(f'Olá {name}, o seu primeiro nome é muito grande!')
else:
    print(f'Olá {name}, o seu primeiro nome tem o tamanho normal.')

