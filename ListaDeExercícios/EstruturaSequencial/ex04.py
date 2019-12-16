'''
Faça um programa que peça as 4 notas bimestrais e mostre a média.
'''
cont = 1
soma = 0
for número in range(1,5):
    nota = float(input('Digite a nota {}: '.format(cont)))
    cont += 1
    soma += nota
print('Média das notas: {:.2f}'.format(soma/4))