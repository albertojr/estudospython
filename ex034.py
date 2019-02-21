salario = float(input('Digite o salário do funcionário R$: '))
if salario > 1250:
    calc = salario * 0.10 + salario
    print('Seu salário de {} tem 10% de aumento, logo o novo valor será {}'.format(salario, calc))
else:
    calc = salario * 0.15 + salario
    print('Seu salário de {} tem 15% de aumento, logo o novo valor será {}'.format(salario, calc))

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.