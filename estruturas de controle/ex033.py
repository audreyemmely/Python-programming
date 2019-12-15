'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint

contVitória = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]\n')).strip().upper()[0]
    print('\nVocê jogou {} e o computador jogou {}. Total de {} '.format(jogador, computador, total), end ='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            contVitória += 1
        else:
            print('Você perdeu :(')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            contVitória += 1
        else:
            print('Você perdeu :(')
            break
    print('\nVamos jogar novamente...')
print('\nGAME OVER! Você venceu {} vezes.'.format(contVitória))
 