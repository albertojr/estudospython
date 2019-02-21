"Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a"
"maioridade e quantas já são maiores."
from datetime import date
maiorIdade = 0
for i in range(0, 7):
    dt = int(input('Digite a data de nascimento: '))
    if (date.today().year - dt) < 21:
        maiorIdade += 1
print('{} pessoas não atingiram a maior idade penal'.format(maiorIdade))
print('{} pessoas são maiores de idade'.format(7-maiorIdade))