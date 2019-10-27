'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite seu nome:\n')).strip() #strip elimina os espaços antes e depois da string
print('\nSeu nome com letras maiúsculas:\n{}'.format(nome.upper()))
print('Seu nome com letras minúsculas:\n{}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))