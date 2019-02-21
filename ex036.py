valorCasa = float(input('Digite o valor da casa: '))
salarioComprador = float(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos vai pagar a casa? '))
prestaçãoMensal = valorCasa / (12*anos)
limitedeEmprestimo = salarioComprador * 0.30

print('O valor da prestação mensal é de R$ {:0.2f}'.format(prestaçãoMensal))

if prestaçãoMensal<=limitedeEmprestimo:
    print('O seu empréstimo foi aprovado, parabéns!!')
else:
    print('O seu empréstimo foi negado!!')
