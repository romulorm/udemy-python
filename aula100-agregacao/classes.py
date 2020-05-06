class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []


    def adiciona_produto(self, produto):
        self.produtos.append(produto)


    def lista_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome:<15} R$ {produto.preco:.2f}')


    def calcula_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        print(f'\33[32mTotal carrinho: R$ {total:.2f}\33[m')


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco