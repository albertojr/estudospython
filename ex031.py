distância = float(input('Digite a distância da viagem em KM: '))
if distância <= 200:
    print('O valor da passagem é: {} R$'.format(distância*0.50))
else:
    print('O valor da passagem é: {} R$'.format(distância*0.45))

#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.