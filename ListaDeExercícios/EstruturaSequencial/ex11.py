'''
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
from math import pow
num1 = int(input('Digite um número inteiro: ')) 
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))
produto = (num1*num1) * (num2/2)
soma = (num1*3) + num3
cubo = pow(num3, 3)
print(f'Produto: {produto}')
print(f'Soma: {soma}')
print(f'Cubo: {cubo}')