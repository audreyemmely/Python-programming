'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
metros = float(input('Qual o tamanho da área a ser pintada, em metros quadrados? '))
litros = metros / 3

if metros % 54 == 0: #(18*3) = 54
    latas = metros / 54
else:
    latas = int(metros/54)+1

preço = latas * 80
print('{}'.format(latas))
print('R$ %.2f' %preço)