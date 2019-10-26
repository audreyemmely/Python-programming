'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''
from math import hypot
catetoO = float(input('Insira o valor do cateto oposto:\n'))
catetoA = float(input('Insira o valor do cateto adjacente:\n'))
hipotenusa = hypot(catetoO, catetoA)
print('A hipotenusa desse triângulo é {:.2f}'.format(hipotenusa))
