"Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade "
"do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."

idades: int = 0
maisVelho: int = 0
OVelho: str
contMulheres = 0
for i in range(1, 5):
    print('-------------- {}ª pessoa --------------'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().lower()
    print()
    idades += idade
    if idade > maisVelho:
        maisVelho = idade
        OVelho = nome
    if sexo in 'f' and idade < 20:
        contMulheres += 1
print('Média de Idade:{} '.format(idades/4))
print('O ou A mais velho(a) é {}'.format(OVelho))
print('{} Mulheres tem menos de 20 anos'.format(contMulheres))