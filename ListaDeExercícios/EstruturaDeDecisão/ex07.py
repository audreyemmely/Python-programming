'''
Faça um programa que leia três números e mostre o maior e o menor deles.
'''
primeiro = float(input('Primeiro número: '))
segundo = float(input('Segundo número: '))
terceiro = float(input('Terceiro número: '))

maior = primeiro
menor = primeiro

if maior < segundo:
    maior = segundo

if maior < terceiro:
    maior = terceiro

if menor > segundo:
    menor = segundo

if menor > terceiro:
    menor = terceiro

print('\nMaior: %.2f ' %maior)
print('Menor: %.2f ' %menor)