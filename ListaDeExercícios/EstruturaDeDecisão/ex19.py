'''
Faça um programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''
número = int(input('Digite um número inteiro: '))
if número%2 == 0:
    print('Número par') 
else:
    print('Número ímpar')