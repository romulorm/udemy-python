class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def falar(self):
        print(f'{self.nome} está falando.')


class Cliente(Pessoa):
    def comprar(self, produto):
        print(f'{self.nome} está comprando {produto}.')


class Aluno(Pessoa):
    def estudar(self, assunto):
        print(f'{self.nome} está estudando {assunto}.')
