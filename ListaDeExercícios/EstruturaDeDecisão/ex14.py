'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1+nota2)/2
if média >= 9 and média <= 10:
    print('Nota 1: {:.2f}\nNota 2: {:.2f}'.format(nota1, nota2))
    print('Média: {:.2f}'.format(média))
    print('Conceito A.\nAprovado!')  
elif média >= 7.5 and média < 9:
    print('Nota 1: {:.2f}\nNota 2: {:.2f}'.format(nota1, nota2))
    print('Média: {:.2f}'.format(média))
    print('Conceito B.\nAprovado!')  
elif média >= 6 and média < 7.5:
    print('Nota 1: {:.2f}\nNota 2: {:.2f}'.format(nota1, nota2))
    print('Média: {:.2f}'.format(média))
    print('Conceito C.\nAprovado!')  
elif média >= 4 and média < 6:
    print('Nota 1: {:.2f}\nNota 2: {:.2f}'.format(nota1, nota2))
    print('Média: {:.2f}'.format(média))
    print('Conceito D.\nReprovado!')  
elif média >= 0 and média < 4:
    print('Nota 1: {:.2f}\nNota 2: {:.2f}'.format(nota1, nota2))
    print('Média: {:.2f}'.format(média))
    print('Conceito E.\nReprovado!')
else:
    print('Algo deu errado. Tente novamente!')