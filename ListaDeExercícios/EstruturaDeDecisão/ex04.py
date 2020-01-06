'''
Faça um programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = str(input('Digite uma letra: ')).upper()
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('A letra é uma vogal.')
else:
    print('A letra é uma consoante.')
