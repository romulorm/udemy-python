'''
Crie uma função que recebe 3 números e retorne a soma deles.
'''

def somatres(n1, n2, n3):
    return n1 + n2 + n3


# PROGRAMA PRINCIPAL
numeros = list()

for n in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
n1, n2, n3 = numeros #desempacotamento
resultado = somatres(n1, n2, n3)
print(f'A soma dos três números é {resultado}')