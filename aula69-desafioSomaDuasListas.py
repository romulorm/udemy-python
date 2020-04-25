'''
Somar duas listas de acordo com a menor.
'''

lista1 = [1, 2, 3, 4, 5, 6]
lista2= [1, 2, 3, 4]

'''
Solução em programação geral
'''
lista_soma = []
for i in range(len(lista2)):
    lista_soma.append(lista1[i] + lista2[i])
print(f'Resultado com a Solução em programação geral: {lista_soma}')

'''
Solução específica da linguagem Python.
'''
lista_soma2 = [x + y for x, y in zip(lista1, lista2)]
print(f'Resultado com a Solução específica da linguagem Python: {list(lista_soma2)}')

'''
Somar duas listas de acordo com a maior usando zip_longest
'''
from itertools import zip_longest

lista_soma3 = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)]
print(f'Resultado com a solução usando zip_longest: {list(lista_soma3)}')
