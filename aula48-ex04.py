'''
Fizz Buzz
Se o parâmetro da função for divisível por 3, retorne fizz.
Se o parâmetro da função for divisível por 5, retorne buzz.
Se o parâmetro da função for divisível por 3 e por 5, retorne fizzbuzz, caso contrário, retorne o número enviado.
'''

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return n

# PROGRAMA PRINCIPAL

print(fizzbuzz(7))
