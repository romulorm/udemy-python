'''
Construa um validador de CPF

04.252.011/0001-10
1) Primeira validação:
Multiplicar cada dígito do CPF pelos dígitos do validador
CPF:       042520110001
VALIDADOR: 543298765432
1.1) Pegar o resultado da multiplicação (65 no exemplo) e usar na fórmula: 11 - (65 % 11) = 1
Se for maior que 9, se torna 0.

2)Segunda validação:
É incluído o dígito calculado na primeira validação e o validador passa a iniciar com 6.

CPF:       0425201100011
VALIDADOR: 6543298765432

2.1) Pegar o resultado da multiplicação (67 no exemplo) e usar na fórmula: 11 - (65 % 11) = 11
Se for maior que 9, se torna 0.

'''

while True:
    input_cnpj = input('Digite o CNPJ completo, sem hífen ou pontos. (x para SAIR): ')
    if input_cnpj == 'x':
        print('Programa finalizado!')
        exit(0)

    dv1 = dv2 = total = 0
    cnpj = input_cnpj[:12]
    validador1 = '543298765432'
    validador2 = '6543298765432'

    # VALIDAÇÃO DO PRIMEIRO DÍGITO

    for i in range(0, 12):
        total += int(cnpj[i]) * int(validador1[i])
    valida_digito = 11 - (total % 11)
    if valida_digito > 9:
        dv1 = 0
    else:
        dv1 = valida_digito

    # VALIDAÇÃO DO SEGUNDO DÍGITO
    cnpj = cnpj + str(dv1)
    total = 0
    for i in range(0, 13):
         total += int(cnpj[i]) * int(validador2[i])
    valida_digito = 11 - (total % 11)
    if valida_digito > 9:
        dv2 = 0
    else:
        dv2 = valida_digito
    cnpj = cnpj + str(dv2)

    print(f'CNPJ inserido:  {input_cnpj}')
    print(f'CNPJ calculado: {cnpj}')
    if input_cnpj == cnpj:
        print('\33[32mCNPJ válido\33[m')
    else:
        print('\33[31mCNPJ inválido\33[m')
    print('\33[34m-------------------------------\33[m')
