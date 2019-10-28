'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randrange
numeroComputador = randrange(0,6)
#print(numeroComputador)
numeroUsuario = int(input('Digite o número que você acha que o computador escolheu (entre 0 e 5):\n'))
if numeroComputador == numeroUsuario:
    print('Você venceu!')
else:
    print('Você perdeu :(')
