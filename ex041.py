from datetime import date
anoNascimento  = int(input('Digite o ano de Nascimento: '))
idade = date.today().year - anoNascimento

if idade <= 9:
    print('Sua categoria é MIRIM')
elif  idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')
