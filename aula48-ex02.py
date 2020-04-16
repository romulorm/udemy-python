'''
Crie uma função que recebe 3 números e retorne a soma deles.
'''

def somatres(n1, n2, n3):
    return n1 + n2 + n3


# PROGRAMA PRINCIPAL
numeros = list()

for n in range(0, 3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

resultado = somatres(numeros[0], numeros[1], numeros[2])
print(f'A soma dos três números é {resultado}')