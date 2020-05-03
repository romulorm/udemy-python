from random import randint

cnpj = str(randint(100000000000, 999999999999))
dv1 = dv2 = total = 0
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

print(f'CNPJ calculado: \33[32m{cnpj}\33[m')

