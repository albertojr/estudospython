r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print('dá pra formar um triângulo')
else:
    print('não dá pra formar um triângulo')











#Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

#soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.