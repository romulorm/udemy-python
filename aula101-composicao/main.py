from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 33)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.insere_endereco('Brasília', 'DF')
cliente3 = Cliente('João', 40)
cliente3.insere_endereco('Salvador', 'BA')

print(cliente1.nome)
Cliente.lista_enderecos(cliente1)
print()
print(cliente2.nome)
Cliente.lista_enderecos(cliente2)
print()
print(cliente3.nome)
Cliente.lista_enderecos(cliente3)

# se der um "del cliente1", o cliente Luiz será apagado juntamente com o seu endereço Belo Horizonte.
