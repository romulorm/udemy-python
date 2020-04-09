'''
Faça um programa que pergunte o nome ao usuário e, basenado-se no horário atual, exiba a saudação apropriada:
Bom dia: 0h-11h, Boa tarde: 12-17, Boa noite: 18h-23
'''

from datetime import datetime

saudacao = ''
nome = str(input('Olá que qual o seu nome? '))
h = datetime.now().hour
if 0 <= h <= 11:
    saudacao = 'Bom dia'
elif 12 <= h <= 17:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite!'
print(f'{saudacao}, {nome}.')