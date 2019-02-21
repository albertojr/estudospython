numero = int(input('Digite um numero entre 0 a 9999:'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade.: {}'.format(unidade))
print('Dezenha: {}'.format(dezena))
print('Centena: {}'.format(centena))
print("Milhar: {}".format(milhar))