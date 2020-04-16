'''
Crie uma função que receba 2 números. O primeiro é um preço e o segundo é um percentual. A função retornará o valor
corrigido com o percentual.
'''

def reajuste(valor, percent):
    return valor + valor * (percent/100)


v = float(input('Digite o valor a sofrer reajuste (R$): '))
p = float(input('Digite o percentual de reajuste (%): '))
valorreajustado = reajuste(v, p)
print(f'\33[32mValor de R${v:.2f} reajustado em {p}% = R${valorreajustado:.2f}\33[m')
