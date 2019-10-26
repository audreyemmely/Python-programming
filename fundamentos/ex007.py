'''
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
largura = float(input('Largura da parede:\n'))
altura = float(input('Altura da parede:\n'))
área = largura * altura
tinta = área/2
print('Sua parede tem dimensão de {}x{} e sua área é de {:.2f}m².\nPara pintar essa parede você precisára de {:.2f}l de tinta'.format(largura, altura, área, tinta))