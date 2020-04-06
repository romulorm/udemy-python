from datetime import datetime

nome = 'Luiz Otávio'
ano_nasc = 1987
altura = 1.80
peso = 80
imc = peso / (altura ** 2)
idade = datetime.now().year - ano_nasc

print(f'{nome} tem {idade} anos, {altura:.2f} de altura.')
print(f'Ele pesa {peso}kg e o IMC dele é {imc:.2f}.')
