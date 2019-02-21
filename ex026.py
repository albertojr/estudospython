nome = str(input('Digite uma frase:\n')).lower().strip()
print('A letra a aparece {} vezes'.format(nome.count('a')))
print('A letra a aparece pela 1º vez na posição {}'.format(nome.find('a')+1))
print('A letra A aparece pela última vez na posição {}'.format(nome.rfind('a')+1))


