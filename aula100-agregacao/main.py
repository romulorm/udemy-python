from classes import CarrinhoDeCompras, Produto

p1 = Produto('Caneta', 1.50)
p2 = Produto('Borracha', 3.50)
p3 = Produto('Lápis', 1.00)
p4 = Produto('Apontador', 5.50)

carrinho = CarrinhoDeCompras()
carrinho.adiciona_produto(p1)
carrinho.adiciona_produto(p2)
carrinho.adiciona_produto(p3)
carrinho.adiciona_produto(p4)
carrinho.lista_produtos()
carrinho.calcula_total()