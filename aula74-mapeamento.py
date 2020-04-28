from dados import produtos

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.1, 2)
    return p


nova_lista = map(aumenta_preco, produtos)

for produto in nova_lista:
    print(produto)