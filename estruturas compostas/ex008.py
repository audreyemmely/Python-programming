'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip()
    if resp not in 'Ss':
        break
print('-='*25)
numeros.sort()
print(f'Voce digitou os valores {numeros}')