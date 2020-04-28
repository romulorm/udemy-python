a = 1
try:
    print(b)
except NameError as erro:
    print('Erro: A variável não existe.')
except Exception as erro: # demais erros
    print('Ocorreu outro erro.')
else:
    print('Esse bloco será executado somente se não houver erros.')
finally:
    print('Esse bloco finally sempre será executado.')