l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [v * 3 for v in l1]

print(l2)

# gera um set
d1 = {x for x in range(5)}
print(d1, type(d1))

# gera um dicionário, ou seja, com chave e valor.
d2 = {f'id{x}': x**2 for x in range(5)}
print(d2)

lista = list(range(100))
print(lista)