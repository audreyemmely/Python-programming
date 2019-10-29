'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
anonasc = int(input('Digite o ano de nascimento:\n'))
idade = date.today().year - anonasc #2019 é o ano atual

if idade < 18:
    print('Você ainda vai se alistar! Faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Você já deveria ter se alistado! Está {} anos atrasado.'.format(idade - 18))    
else:
    print('Está na idade para se alistar!')