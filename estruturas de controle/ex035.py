'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
totalCompra = maiorQueMil = menorPreço = contador = 0
prodBarato = ''
while True:
    print('~'*30)
    print('LOJINHA DA AU')
    print('~'*30)
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    contador += 1
    totalCompra += preço
    if preço > 1000:
        maiorQueMil += 1
    if contador == 1 or preço < menorPreço:
        menorPreço = preço
        prodBarato = produto
    decisão = ' '
    while decisão not in 'SN':
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if decisão == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('\nO total da compra foi R${:.2f}'.format(totalCompra))
print('Temos {} produtos custando mais de R$1000.00'.format(maiorQueMil))
print('O produto mais barato foi {}, e custa R${:.2f}'.format(prodBarato, menorPreço))
