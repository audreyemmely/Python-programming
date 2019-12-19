'''
Faça um programa que peça dois números e imprima o maior deles.
'''
número1 = float(input('Digite o primeiro número: '))
número2 = float(input('Digite o segundo número: '))
if número1 > número2:
    print('Entre {} e {}, o maior valor é {}'.format(número1, número2, número1))
else:
    print('Entre {} e {}, o maior valor é {}'.format(número1, número2, número2))