num = int(input('Digite um numero: '))
contNum = 0
totNum = 0
while num != 99:
    totNum += num
    num = int(input('Digite um numero: '))
    contNum += 1
print('Foram digitados {} Números'.format(contNum))
print('Somátorio dos números digitados {}'.format(totNum))
