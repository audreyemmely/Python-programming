'''
Altere o programa anterior (ex04) permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''
ano = 0
popA = float(input('Informe a população A: '))
taxaA = float(input('Insira a taxa de crescimento anual da população A: '))
while popA <= 0:
    popA = float(input('A população precisa ser maior que 0 (zero). Informe novamente a população A: '))
popB = float(input('\nInforme a população B: '))
taxaB = float(input('Insira a taxa de crescimento anual da população B: '))
while popB <= 0:
    popB = float(input('A população precisa ser maior que 0 (zero). Informe novamente a população B: '))

while popA < popB:
    ano += 1
    popA = popA + (popA * 0.03)
    popB = popB + (popB * 0.015)

print(f'\nNúmero de anos necessários para que a população A ultrapasse ou iguale à população B: {ano}')