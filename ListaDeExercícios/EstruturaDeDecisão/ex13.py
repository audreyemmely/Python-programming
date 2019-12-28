'''
Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
número = int(input('Digite um número entre 1 e 7: '))
if número == 1:
    print('1 - Domingo')
elif número == 2:
    print('2 - Segunda')
elif número == 3:
    print('3 - Terça')
elif número == 4:
    print('4 - Quarta')
elif número == 5:
    print('5 - Quinta')
elif número == 6:
    print('6 - Sexta')
elif número == 7:
    print('7 - Sábado')
else:
    print('Valor inválido')