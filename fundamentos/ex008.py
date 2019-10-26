'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
com 5% de desconto.
'''
preço = float(input('Qual é o preço do produto?\nR$ '))
novo = preço - (preço*0.05)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}.'.format(preço, novo))