'''
Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * (9/5)) + 32
print('Temperatura em Fahrenheit: {:.2f} °F'.format(fahrenheit))