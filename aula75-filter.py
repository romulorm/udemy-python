from dados import produtos

nova_lista = filter(lambda p: p['preco'] > 10, produtos)
print(list(nova_lista))