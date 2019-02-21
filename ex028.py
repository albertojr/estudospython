import random
numero = random.randint(0, 5) #aqui ele pensa em um número ...
print('-=-'*20)
print('Estou pensando em um pensando em um número de 0 a 5 ... AGUARDE!')
print('-=-'*20)
numeroDigitado = int(input('Tente adivinhar meu número, digite abaixo: '))
if numero == numeroDigitado:
    print('Parabéns, vc adivinhou, tu é FODA!!')
else:
    print('ERROOOOOOOOU!!!!')
