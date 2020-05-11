'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
lista = []
posicao_maior = []
posicao_menor = []
for posicao in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {posicao}: ')))
for index, valor in enumerate(lista):
    if valor == max(lista):
        posicao_maior.append(index)
    if valor == min(lista):
        posicao_menor.append(index)
print('-*'*27)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)}, nas posicoes {posicao_maior}')
print(f'O menor valor digitado foi {min(lista)}, nas posicoes {posicao_menor}')
print()