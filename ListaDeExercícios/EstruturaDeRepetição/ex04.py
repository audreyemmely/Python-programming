'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
popA = 80000
popB = 200000
ano = 0

while popA < popB:
    ano += 1
    popA = popA + (popA * 0.03)
    popB = popB + (popB * 0.015)

print(f'Número de anos necessários para que a população A ultrapasse ou iguale à população B: {ano}')
    