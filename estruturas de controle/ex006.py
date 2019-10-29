'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date

anonasc = int(input('Qual o ano de nascimento do atleta?\n'))
idade = date.today().year - anonasc
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade > 19 and idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')        