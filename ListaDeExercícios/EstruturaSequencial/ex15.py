'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
from math import ceil

área = float(input('Qual o tamanho da área a ser pintada, em metros quadrados? '))
rendLitro = área/6
litroLata = 18
litroGalão = 3.6
preçoLata = 80
preçoGalão = 25
qtdLata = ceil((rendLitro/litroLata)*1.10)
qtdGalão = ceil((rendLitro/litroGalão)*1.10)
compraLata = preçoLata * qtdLata
compraGalão = preçoGalão * qtdGalão
melhorCompraLata = int(rendLitro/litroLata)
melhorCompraGalão = ceil((rendLitro%litroLata)/litroGalão)
mix = (melhorCompraLata*preçoLata)+(melhorCompraGalão*preçoGalão)

print('\nQuantidade de tinta a ser comprada e os preços em três situações')
print('~'*65)
print('1) Comprar apenas latas de 18 litros: \n   Quantidade: {} \n   Preço: R$ {:.2f}'.format(qtdLata, compraLata))
print('2) Comprar apenas galões de 3,6 litros: \n   Quantidade: {} \n   Preço: R$ {:.2f}'.format(qtdGalão, compraGalão))
print('3) Comprar latas e galões pagando o mínimo possível: \n   Quantidade de latas: {} \n   Quantidade de galões: {} \n   Preço: R$ {:.2f}\n'.format(melhorCompraLata, melhorCompraGalão, mix))

if (compraLata < compraGalão):
    if(compraLata < mix):
        print('A MELHOR OPÇÃO DE COMPRA É A Nº 1')
    else:
        print('A MELHOR OPÇÃO DE COMPRA É A Nº 3')
else:
    if(compraGalão < mix):
        print('A MELHOR OPÇÃO DE COMPRA É A Nº 2')
    else:
        print('A MELHOR OPÇÃO DE COMPRA É A Nº 3')