'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
ganhoHora = float(input('Quanto você ganha por horas? R$ '))
horasTrabalhadas = float(input('Quantas horas você trabalhou neste mês? '))
print('Total salário: R$ {:.2f}'.format(ganhoHora*horasTrabalhadas))