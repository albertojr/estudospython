from random import choice
aluno01 = input('Digite o nome do aluno 1: ')
aluno02 = input('Digite o nome do aluno 2: ')
aluno03 = input('Digite o nome do aluno 3: ')
aluno04 = input('Digite o nome do aluno 4: ')
lista = [aluno01, aluno02, aluno03, aluno04] #lista de alunos, em python fica em colchetes
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
