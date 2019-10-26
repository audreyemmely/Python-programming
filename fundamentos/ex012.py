'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
from random import choice

aluno1 = str(input('Primeiro aluno:\n'))
aluno2 = str(input('Segundo aluno:\n'))
aluno3 = str(input('Terceiro aluno:\n'))
aluno4 = str(input('Quarto aluno:\n'))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))