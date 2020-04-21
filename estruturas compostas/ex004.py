'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

numeros = tuple(int(input('Digite o {} numero:'.format(i+1))) for i in range(4))
print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vez/vezes')
if 3 in numeros:
  print(f'O valor 3 apareceu na {numeros.index(3)+1} posicao')
else:
  print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for n in numeros:
  if n%2 == 0:
    print(n, end = ' ')
