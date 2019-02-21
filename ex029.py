velocidade = float(input('Digite a velocidade do carro em KM: '))
if velocidade > 80:
    print('PARABÉNS! vc foi multado, valor a pagar: R${}'.format((velocidade-80)*7))
print('Dirija com segurança! ;)')
