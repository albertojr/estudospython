from random import choice
lista = ('pedra', 'papel', 'tesoura')
escolhaPC = choice(lista)
escolhaJogador = str(input('Digite sua jogada ENTRE pedra, papel ou tesoura:\n').lower().strip())

if escolhaPC in 'pedra' and escolhaJogador in 'tesoura':
    print('O pczaum da massa ganhou!')
    print('O pc escolheu {} e vc escolheu {}'.format(escolhaPC, escolhaJogador))

elif escolhaPC in 'pedra' and escolhaJogador in 'papel':
    print('você ganhou! o computador escolheu {} e você escolheu {}'.format(escolhaPC,escolhaJogador))

elif escolhaPC in 'pedra' and escolhaJogador in 'pedra':
    print('Empatado!! o computador escolheu {} e vc escolheu {}'.format(escolhaPC, escolhaJogador))

elif escolhaPC in 'tesoura' and escolhaJogador in 'pedra':
    print('Vc ganhou!! o PC escolheu {} e vc escolheu {}'.format(escolhaPC, escolhaJogador))

elif escolhaPC in 'tesoura' and escolhaJogador in 'papel':
    print('O PC ganhou!! O PC escolheu {} e vc escolheu {}'.format(escolhaPC, escolhaJogador))

elif escolhaPC in 'tesoura' and escolhaJogador in 'tesoura':
    print('EMPATE!!! vc escolheu {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))

elif escolhaPC in 'papel' and escolhaJogador in 'papel':
    print('EMPATE!!! vc escolheu {} e vc escolheu {}'.format(escolhaJogador, escolhaPC))

elif escolhaPC in 'papel' and escolhaJogador in 'tesoura':
    print('Vc ganhou!! o PC escolheu {} e vc escolheu {}'.format(escolhaPC, escolhaJogador))

elif escolhaPC in 'papel' and escolhaJogador in 'pedra':
    print('O PC ganhou!! O PC escolheu {} e vc escolheu {}'.format(escolhaPC, escolhaJogador))
