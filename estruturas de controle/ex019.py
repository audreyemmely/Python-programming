'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano {} a pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >=18:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('Ao todo tivemos {} menores de idade'.format(totalMenor))