somatorio = 0
for i in range(0, 6):
    s = int(input('Digite um número: '))
    if s % 2 == 0:
       somatorio += s
print('O valor final do somatório dos números pares é {}'.format(somatorio))
