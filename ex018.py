from math import cos,sin,tan,radians
angulo = int(input('Digite o valor do ângulo: '))
rad = radians(angulo)
cosseno = cos(rad)
seno = sin(rad)
tangente = tan(rad)
print('O ângulo {} tem\n seno: {:0.2f}\n cosseno:{:0.2f}\n Tangente:{:0.2f}'.format(angulo,seno, cosseno, tangente))
