'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
primeiro = float(input('Digite o primeiro número:\n'))
segundo = float(input('Digite o segundo número:\n'))
terceiro = float(input('Digite o terceiro número:\n'))
numeros = [primeiro, segundo, terceiro]

print('O maior número é {}'.format(max(numeros)))
print('O menor número é {}'.format(min(numeros)))