"Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, "
"desconsiderando os espaços."
frase = str(input('Digite a frase: ')).strip().upper()
fraseSemEspaço = frase.replace(' ', '')
inverso = ''
t = 0
for i in range(len(fraseSemEspaço)-1, -1, -1):
    inverso += fraseSemEspaço[i]
print('O inverso de {} é {}'.format(fraseSemEspaço, inverso))
if fraseSemEspaço in inverso:
    print('temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
