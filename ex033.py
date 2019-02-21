#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o 1º Número: '))
num2 = float(input('Digite o 2º Número: '))
num3 = float(input('Digite o 3º Número: '))

if num1 > num2 and num1 > num3 and num2 < num3:
    print("{} é o maior\nO menor número é {}".format(num1, num2))
    #numero 1 > num2 e num 3, num 2 menor do que num3
if num1 > num2 and num1 > num3 and num3 < num2:
    print("{} é o maior\nO menor número é {}".format(num1, num3))
    #numero 1 > num2 e num 3, num 3 menor do que num 2
if num2 > num1 and num2 > num3 and num1 < num3:
    print("{} é o maior\nO menor número é {}".format(num2, num1))
    # numero 2 > num1 e num 3, num 1 menor do que num2
if num2 > num1 and num2 > num3 and num3 < num1:
    print("{} é o maior\nO menor número é {}".format(num2, num3))
    # numero 2 > num1 e num 3, num3 menor do que num1
if num3 > num2 and num3 > num1 and num1 < num2:
    print("{} é o maior\nO menor número é {}".format(num3, num1))
    #num3 > num1 e num2, num1 menor do que num2
if num3 > num1 and num3 > num2 and num2 < num1:
    print("{} é o maior\nO menor número é {}".format(num3, num2))
    #num3 > num1 e num2, num2 menor do que num1