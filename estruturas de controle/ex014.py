'''
Refaça o DESAFIO 005 (fundamentos), mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.
'''
numero = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, numero*c))