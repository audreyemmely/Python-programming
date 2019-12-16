'''
Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
'''
from math import pi, pow
raio = float(input('Digite o raio do círculo: '))
área = pi * pow(raio,2)
print('Área do circulo: {}'.format(área))