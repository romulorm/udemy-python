from random import randint

total = result = dv1 = dv2 = 0
cpf_sem_dv = cpf_com_dv1 = ''

for v in range(0, 9):
    cpf_sem_dv += str(randint(0, 9))
for i, c in enumerate(range(10, 1, -1)):
    result = c * int(cpf_sem_dv[i])
    total += result
dv1 = 11 - (total % 11)
if dv1 > 9:
    dv1 = 0
cpf_com_dv1 = cpf_sem_dv + str(dv1)
result = total = 0
for i, c in enumerate(range(11, 1, -1)):
    result = c * int(cpf_com_dv1[i])
    total += result
dv2 = 11 - (total % 11)
if dv2 > 9:
    dv2 = 0
cpf_calculado = cpf_sem_dv + str(dv1) + str(dv2)
print(f'CPF gerado = \33[36m{cpf_calculado}\33[m')
