'''
Faça um programa que leia três números e mostre o maior deles.
'''
primeiro = float(input('Primeiro número: '))
segundo = float(input('Segundo número: '))
terceiro = float(input('Terceiro número: '))

maior = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
print('Maior: {:.2f}'.format(maior))