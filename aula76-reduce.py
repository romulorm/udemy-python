from dados import lista, produtos, clientes
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)

soma_idades = reduce(lambda ac, i: i['idade'] + ac, clientes, 0)
print(f'Média das idades dos clientes: {round(soma_idades / len(clientes))}')