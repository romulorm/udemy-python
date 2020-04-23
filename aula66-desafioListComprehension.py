'''
Desenvolver um somador do carrinho de compras utilizando List Comprehension.
'''

carrinho = []
carrinho.append(('Produto 1', 30.10))
carrinho.append(('Produto 2', 20.99))
carrinho.append(('Produto 3', 50.01))

total = sum([float(y) for x, y in carrinho])
print(f'Total (R$): {total:.2f}')