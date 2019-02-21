num = int(input('Digite um numero inteiro: '))
print('Escolha uma opção para conversão:\n1 - para binário\n2 - para octal\n3 - para hexadecimal\n ')
escolha = int(input('Digite: '))

if escolha == 1:
    print('O {} em binário é {}'.format(num, bin(num)[2:]))#pula as duas primeiras letras da STRING
elif escolha == 2:
    print('O {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('alternativa errada, escolha novamente')


#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para
# o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.