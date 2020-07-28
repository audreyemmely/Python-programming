'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N' or resp not in 'SN':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('~*'*30)
print(f'\nTodos os valores digitados: {lista}')
print(f'Valores pares: {pares}')
print(f'Valores ímpares: {impares}')