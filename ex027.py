nome = str(input('Digite o nome completo: ')).strip()
primeiroNome = nome.split()
print('Muito prazer em te conhecer!')
print('O primeiro nome é {}'.format(primeiroNome[0]))
print('O último nome de {} é...\n{}'.format(nome, primeiroNome[len(primeiroNome)-1]))
