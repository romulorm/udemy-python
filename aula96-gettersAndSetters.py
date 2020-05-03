'''
Getter and Setter - Possibilita filtrar as entradas sem precisar alterar o código da aplicação.
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, porcentagem):
        self.preco = self.preco - self.preco * (porcentagem / 100)


    #Getter
    @property
    def preco(self):
        return self._preco


    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor



# PROGRAMA PRINCIPAL
p1 = Produto('Camisa', 30)
p1.desconto(10)
print(p1.preco)

# ENTRADA COM ERRO (STRING COM R$) FUNCIONANDO GRAÇAS AO SETTER
p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)
