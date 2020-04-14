total = total2 = result = v = v2 = dv1 = dv2 = result2 = 0
cpf_com_digito1 = ''

cpf = str(input('Digite o CPF \33[33m(sem pontos ou hífen)\33[m: '))
cpf_sem_dv = cpf[0:9]
for i, c in enumerate(range(10, 1, -1)):
    result = c * int(cpf_sem_dv[i])
    total += result
v = 11 - (total % 11)
if v > 9:
    dv1 = 0
else:
    dv1 = v
cpf_com_digito1 = cpf_sem_dv + str(dv1)
for i2, c2 in enumerate(range(11, 1, -1)):
    result2 = c2 * int(cpf_com_digito1[i2])
    total2 += result2
v2 = 11 - (total2 % 11)
if v2 > 9:
    dv2 = 0
else:
    dv2 = v2
cpf_calculado = cpf_sem_dv + str(dv1) + str(dv2)
print(f'CPF digitado  = \33[36m{cpf}\33[m')
print(f'CPF calculado = \33[36m{cpf_calculado}\33[m')
if cpf == cpf_calculado:
    print('\33[34mCPF validado com sucesso!\33[m')
else:
    print('\33[31mCPF inválido!\33[m')
