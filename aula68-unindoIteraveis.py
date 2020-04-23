'''
zip - unindo iteráveis de acordo com a menor lista
zip_longest - une iteráveis mesmo sem pares
'''
from itertools import zip_longest


estados = ['SP', 'MG', 'BA']

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

cidades_estados = zip(estados, cidades)
print(list(cidades_estados))

cidades_estados = zip_longest(estados, cidades, fillvalue='UF')
print(list(cidades_estados))
