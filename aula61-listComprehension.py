'''
Gerar uma sequência conforme abaixo com a string "string".
0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789
'''

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

passo = 10
contadores = [i for i in range(0, len(string), passo)]
print(contadores)
tuplas = [(i, i + passo) for i in range(0, len(string), passo)]
print(tuplas)
lista = [string[i:i + passo] for i in range(0, len(string), passo)]
print(lista)
resultado = '.'.join(lista)
print(resultado)
