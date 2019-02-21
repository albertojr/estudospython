preçoNormal = float(input('Digite o preço R$: '))
condiçãoPagamento = int(input('Digite a forma de pagamento:\n1 - à vista\n2 - 2x no Cartão\n3 - 3x ou mais\n'))
if condiçãoPagamento == 1:
    avista = int(input('Digite 1 para pagamento à vista em dinheiro ou 2 para pagamento a vista no cartão: '))
    if avista == 1:
        print('vc tem o desconto de 10%, o valor a pagar é {:0.2f}'.format(preçoNormal-preçoNormal*0.10))
    elif avista == 2:
        print('Vc tem o desconto de 5%, o valor a pagar é {:0.2f}'.format(preçoNormal - preçoNormal * 0.05))
elif condiçãoPagamento == 2:
    print('Não tem desconto, seu preço é {:0.2f}'.format(preçoNormal))
elif condiçãoPagamento == 3:
    print('O preço a pagar é {:0.2f}'.format(preçoNormal + preçoNormal*0.20))
else:
    print('Escolha incorreta, tente novamente!!!!!')
