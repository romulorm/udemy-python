'''
RAISE: Cria uma exceção personalizada do erro.
'''

def dividir(n1, n2):
    if n2 == 0:
        raise ValueError('Não é possível a divisão por ZERO')
    else:
        return n1 / n2

# PROGRAMA PRINCIPAL

print(dividir(2, 0))