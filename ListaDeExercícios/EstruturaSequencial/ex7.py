'''
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
medidaLado = float(input('Digite a medida de um dos lados do quadrado (cm): '))
área = pow(medidaLado, 2)
print('Área do quadrado: {:.2f}cm²'.format(área))
print('Dobro da área: {:.2f}cm²'.format(área*2))
