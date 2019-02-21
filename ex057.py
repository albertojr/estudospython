sexo = str(input('Digite o Sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos,Digite corretamente!: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
