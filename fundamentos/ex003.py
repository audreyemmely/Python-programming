# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))

media = (nota1 + nota2) / 2
print('A média do aluno é: {:.2f}'.format(media))
