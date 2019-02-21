from datetime import date
anoNascimento = int(input('Digite o ano de seu nascimento: '))
idadeUser = date.today().year - anoNascimento

if idadeUser < 18:
    print('Falta {} ano(s) para você se alistar!'.format(18-idadeUser))
elif idadeUser > 18:
    print('Já se passaram {}ano(s) do seu alistamento'.format(idadeUser-18))
else:
    print('Opa, já tá na hora de se alistar!!!')


#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.