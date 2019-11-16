'''
Crie um programa que mostre na tela todos 
os números pares que estão no intervalo entre 1 e 50.
'''
for n in range(1, 51): #ou range(2, 51, 2) e tira o if
    if n%2 == 0:
        print(n, end=' ')