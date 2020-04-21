'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.
'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    número = int(input('Digite um número de 0 a 10: '))
    if 0 <= número <= 10:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[número]}.')
