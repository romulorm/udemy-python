from classes import Pessoa, Aluno, Cliente

c1 = Cliente('Luiz', 73)
a1 = Aluno('Mauro', 10)

c1.comprar('Smartphone')
#c1.estudar('Matemática') Erro. O Cliente (c1) não possui o método estudar que é específico da classe Aluno.
a1.estudar('Matemática')
