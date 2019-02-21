n1 = float(input('Digite a n1: '))
n2 = float(input('Digite a n2: '))
calcNota = (n1+n2)/2

if calcNota < 5.0:
    print('Sua média é {:.1f}, você foi reprovado'.format(calcNota))
elif calcNota == 5.0 and calcNota < 6.9:
    print('Sua média foi {:.1f}, você tá na recuperação'.format(calcNota))
else:
    print('Sua média foi {:.1f}, você foi aprovado!'.format(calcNota))

#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO