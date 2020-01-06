'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
primeiro = float(input('Preço primeiro produto: R$ '))
segundo = float(input('Preço segundo produto: R$ '))
terceiro = float(input('Preço terceiro produto: R$ '))

menor = primeiro

if segundo < menor:
    menor = segundo

if terceiro < menor:
    menor = terceiro

print('\nVocê deve comprar o produto de valor R$ %.2f ' %menor)