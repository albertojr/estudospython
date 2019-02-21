#O ano será bissexto quando ele for divisível por 4. O ano de 2012, por exemplo, é divisível por 4. Logo, é bissexto.
from datetime import date

ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year#pega o ano atual configurado na máquina
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print("Esse ano é BISSEXTO Ó")
else:
    print("O ano {} não é BISSEXTO".format(ano))




#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.