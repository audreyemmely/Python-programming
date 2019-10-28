'''
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
'''
velocidade = int(input('Qual a velocidade do carro?\n'))

if velocidade <= 80:
    print('Tudo bem!')
else:
    multa = (velocidade - 80) * 7
    print('Você foi multado e terá que pagar {:.2f}'.format(multa))