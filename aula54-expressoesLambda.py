'''
Ordenando os produtos em uma lista dentro de outra lista usando as expressões Lambda.
'''

produtos = [
    ['P1', 'Batata', 3.89],
    ['P2', 'Arroz', 16.99],
    ['P3', 'Feijão', 4.59],
    ['P4', 'Macarrão', 3.50],
    ['P5', 'Laranja', 3.99]
]

# Em ordem alfabética
print(sorted(produtos, key=lambda i: i[1]))

# Em ordem de preço
print(sorted(produtos, key=lambda i: i[2]))

# Em ordem de preço (mais caro)
print(sorted(produtos, key=lambda i: i[2], reverse=True))
