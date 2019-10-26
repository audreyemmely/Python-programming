'''
 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
 Considere US$1.00 = R$4.00 (cotação 2019)
'''

real = float(input('Quanto dinheiro você tem na carteira?\n'))
dolar = real/4
print('Com R${:.2f} você pode comprar U$ {:.2f}'.format(real, dolar)) 