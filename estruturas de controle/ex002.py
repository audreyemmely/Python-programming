'''
Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.
'''
numero = int(input('Digite um número:\n'))
escolha = int(input('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal
'''))

if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else: 
    print('Escolha inválida. Tente novamente!')