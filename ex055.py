"Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final,"
"mostre qual foi o maior e o menor peso lidos."
maiorpeso = 0
menorpeso=0
for i in range(0, 5):
    peso = float(input('Digite o peso: '))
    if peso == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        elif peso < maiorpeso:
            menorpeso = peso
print('O maior peso foi de {}Kg'.format(maiorpeso))
print('O menor peso foi de {}Kg'.format(menorpeso))



