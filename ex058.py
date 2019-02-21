"Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. " \
"Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários"
"para vencer."

import random
numero = random.randint(0, 10) #aqui ele pensa em um número ...
totTentativas = 0
print('-=-'*20)
print('Estou pensando em um pensando em um número de 0 a 10 ... AGUARDE!')
print('-=-'*20)
numeroDigitado = int(input('Tente adivinhar meu número, digite abaixo: '))

while numeroDigitado != numero:
    totTentativas += 1
    numeroDigitado = int(input('Vc errou, tente novamente: '))

print('Parabéns, vc acerto em {} tentativas'.format(totTentativas))
