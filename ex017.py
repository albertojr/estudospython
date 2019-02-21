from math import hypot
catetoOposto = float(input('Digite o valor do Cateto Oposto: '))
catetoAdjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('Valor da hipotenusa: {:.2f}'.format(hipotenusa))
