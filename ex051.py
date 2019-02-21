"Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10"
"primeiros termos dessa progressão."

primeirotermo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
print('<>' * 10, 'CÁLCULO DE P.A (PROGRESSÃO ARITIMÉTICA', 10*'<>')
print(primeirotermo)
decimo = primeirotermo+(10-1) * razao
for i in range(primeirotermo, decimo+razao, razao):
    print('{}'.format(i), end='-> ')
print(' acabou!')
