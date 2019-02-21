"Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, "
"com uma pausa de 1 segundo entre eles."

from time import sleep
print('Contagem regressiva para lançamento!')
for n in range(10, -1, -1):
    sleep(0.5)
    print(n)
print('Foguete lançado!')