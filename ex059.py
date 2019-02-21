op = 0
print('-------------- INSIRA 2 NÚMEROS PARA AS OPERAÇÕES -------------')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
while op != 5:
    print('----------- ESCOLHA UMA OPÇÃO -----------')
    op = int(input('1 - SOMAR\n2 - MULTIPLICAR\n3 - MAIOR\n4 - NOVOS NÚMEROS\n5 - SAIR DO PROGRAMA\ndigite aqui: '))
    if op == 1:
        print('Vc escolheu a opção SOMAR! resultado {}\n'.format(num1+num2))
    elif op == 2:
        print('Vc escolheu a opção MULTIPLICAR! resultado {}\n'.format(num1 * num2))
    elif op == 3:
        if num1 > num2:
            print('O {} é o maior'.format(num1))
        elif num2 > num1:
            print('O {} é maior'.format(num2))
        else:
            print('NÃO existe maior, os dois números são iguais!!\n')
    elif op == 4:
        print('Vc escolheu a opção NOVOS NÚMEROS!')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    else:
        print('OPÇÃO INVÁLIDA!!!! Digite a OPÇÃO correta!!')
