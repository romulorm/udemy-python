from pessoa import Pessoa

p1 = Pessoa('Miguel', 8)
p2 = Pessoa('Raphael', 6)

p1.comer('maçã')
p1.falar('informática')
p1.parar_comer()
p1.falar('informática')
print(p1.get_nascimento())
print(p2.get_nascimento())

# Método de classe para gerar um objeto Pessoa de acordo com seu ano de nascimento.
p3 = Pessoa.cria_pessoa_por_ano('Cláudia', 1976)
print(f'{p3.nome} tem {p3.idade} anos.')

# Método Estático para gerar IDs dos objetos:
print(p1.gera_id())
print(p2.gera_id())
print(p3.gera_id())
