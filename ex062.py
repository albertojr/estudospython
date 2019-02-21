primeirotermo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
print('<>' * 10, 'CÁLCULO DE P.A (PROGRESSÃO ARITIMÉTICA', 10*'<>')
print(primeirotermo)
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        primeirotermo = primeirotermo+razao
        print('{}'.format(primeirotermo), end='-> ')
        cont = cont+1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer adicionar? '))
print('Progressão com {} termos'.format(total))
print('FIM')
