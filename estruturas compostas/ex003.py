'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import sample
numeros = tuple(sample(range(10),5)) 
print(numeros)
print(f'O maior valor eh {max(numeros)} e o menor valor eh {min(numeros)}.')
