r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print('dá pra formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é Escaleno')
else:
    print('não dá pra formar um triângulo')

#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes