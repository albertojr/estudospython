from math import pow
peso = float(input('Digite o seu peso kg: '))
altura = float(input('Digite a sua altura: '))
calcIMC = peso / pow(altura, 2)

if calcIMC < 18.5:
    print('Seu IMC é {:.2f}, Vc está abaixo do peso'.format(calcIMC))
elif 18.5 <= calcIMC < 25:
    print('Seu IMC é {:.2f}, Vc está no peso ideal'.format(calcIMC))
elif 25 <= calcIMC < 30:
    print('Seu IMC é {:.2f}, Você está no sobrepeso'.format(calcIMC))
elif 30 <= calcIMC < 40:
    print('Seu IMC é {:.2f}, Você está obeso!'.format(calcIMC))
elif calcIMC >= 40:
    print('Seu IMC é {:.2f}, Você está na obesidade mórbida! '.format(calcIMC))
