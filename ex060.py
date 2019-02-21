num = int(input('Digite um número para fatorial: '))
fat = 1
cont = 1
if num == 0:
    print('O fatorial de {} é 1'.format(num))
else:
    while cont <= num:
        fat = fat * cont
        cont = cont + 1
print('O fatorial de {} é {}'.format(num, fat))

