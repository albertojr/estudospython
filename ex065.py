alt = 'sS'
contNum = 1
totNum = maior = menor = 0
while alt not in 'Nn':
    contNum += 1
    num = int(input('Digite um numero: '))
    totNum += num
    alt = input('Deseja continuar?(S/N): ')[0]
    if num > maior:
        maior = num
    else:
        menor = num

print('Foram digitados {} Números'.format(contNum))
print('Média de todos números digitados {}'.format(totNum/contNum))
if maior == menor:
    print('Não existe número maior ou menor, os 2 são iguais!!!')
else:
    print('O Maior número digitado é {}'.format(maior))
    print('O menor número digitado é {}'.format(menor))
