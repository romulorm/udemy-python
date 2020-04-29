def converte_numero(value):
    if value == 'x':
        print('\33[31mPrograma finalizado pelo usuário!\33[m')
        exit(0)
    else:
        try:
            value = int(value)
            return value
        except ValueError:
            try:
                value = float(value)
                return value
            except Exception:
                pass # vai retornar None


# PROGRAMA PRINCIPAL

while True:
    valor = converte_numero(input('Digite um número (X para sair): ').lower())
    if valor is not None:
        print(f'Valor {valor} multiplicado por 5: \33[33m{valor * 5}\33[m')
    else:
        print('\33[31mInsira um valor válido!\33[m')

