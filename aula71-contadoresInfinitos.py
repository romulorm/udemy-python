'''
Exemplo de utilização do count: Criar índice automático para uma lista.
'''

from itertools import count

contador = count()
lista = ['Luiz', 'Otávio', 'Maria', 'José', 'Silva', 'Eduardo']
lista = zip(contador, lista)
print(list(lista))