'''
Faça um programa que leia um ângulo qualquer 
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
from math import sin, cos, tan, radians
ângulo = float(input('Digite o ângulo que você deseja:\n'))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))

print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))