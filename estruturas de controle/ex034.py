'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''
totalMaisDe18 = totalHomens = totalMenosDe20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*30)
    if idade >= 18:
        totalMaisDe18 += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMenosDe20 += 1
    decisão = ' '
    while decisão not in 'SN':
        decisão = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if decisão == 'N':
        break
print('Total de pesosas com mais de 18 anos: {}'.format(totalMaisDe18))
print('Ao todo temos {} homens cadastrados'.format(totalHomens))
print('E temos {} mulheres com menos de 20 anos'.format(totalMenosDe20))