nome = input("Qual é o seu nome completo?\n")
print('Em Maiscúlo:{}\nEm Minúsculo:{}'.format(nome.upper(), nome.lower()))
#semEspaço = nome.replace(' ', '')
print('Letras sem espaço: {}'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))


