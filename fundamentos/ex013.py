'''
O mesmo professor do ex012 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle

aluno1 = str(input('Primeiro aluno:\n'))
aluno2 = str(input('Segundo aluno:\n'))
aluno3 = str(input('Terceiro aluno:\n'))
aluno4 = str(input('Quarto aluno:\n'))
lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)