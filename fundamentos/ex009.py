'''
 Crie um programa que leia um número real qualquer e mostre na tela a sua parte inteira.
'''
from math import trunc

numero = float(input('Digite um valor:\n'))
print('O valor digitado foi {} e sua parte inteira é {}'.format(numero, trunc(numero)))

#sem usar biblioteca math
numero = float(input('Digite um valor:\n'))
print('O valor digitado foi {} e sua parte inteira é {}'.format(numero, int(numero)))