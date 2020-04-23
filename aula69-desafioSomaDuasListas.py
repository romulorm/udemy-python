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
print(lista_soma)

'''
Solução específica da linguagem Python.
'''
lista_soma2 = [x + y for x, y in zip(lista1, lista2)]
print(list(lista_soma2))
