'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N' or resp not in 'SN':
        break
print('\n')
print('-='*30)
print(f'\nVocê digitou {len(valores)} números.')
print(f'Valores em ordem decrescente: {sorted(valores, reverse = True)}')
if 5 in valores:
    print('O valor 5 está a lista!')
else:
    print('O valor 5 não está na lista!')