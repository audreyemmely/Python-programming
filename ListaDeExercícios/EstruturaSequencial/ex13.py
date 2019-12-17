'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido
'''
salário = float(input('Quanto você ganha por hora? R$ '))
horas = float(input('Quantas horas você trabalhou este mês? '))
salárioBruto = salário * horas
IR = salário - (salário * 0.11)
INSS = salário - (salário * 0.08)
sindicato = salário - (salário * 0.05)
salárioLíquido = salárioBruto - (IR + INSS + sindicato)

print('+ Salário Bruto: R${:.2f}\n'.format(salárioBruto))
print('- IR: R${:.2f}\n'.format(IR))
print('- INSS: R${:.2f}\n'.format(INSS))
print('- Sindicato: R${:.2f}\n'.format(sindicato))
print('= Salário Líquido: R${:.2f}'.format(salárioLíquido))