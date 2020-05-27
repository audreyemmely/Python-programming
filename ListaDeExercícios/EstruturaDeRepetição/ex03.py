'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' = fêmea, 'm' = macho, 'i' = intersexual;
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = str(input('Qual seu nome? '))
idade = int(input('Digite sua idade: '))
salario = float(input('Qual o seu salário? R$ '))
sexo = str(input('Qual o seu sexo biologico? ')).strip().upper()[0]
estado_civil = str(input('Qual o seu estado civil? [casada/o, solteira/o, viúva/o, divorciada/o]\n')).strip().upper()[0]

while len(nome) <= 3:
    nome = str(input('Seu nome deve conter mais de 3 caracteres. Digite seu nome novamente: '))
while idade < 0 or idade > 150:
    idade = int(input('Você deve ter entre 0 e 150 anos. Digite sua idade novamente: '))
while salario < 0:
    salario = float(input('Seu salário precisa ser maior que 0. Digite seu salário novamente: R$ '))
while sexo not in 'FM':
    sexo = str(input('Escolha dentre as opções "feminino", "masculino" ou "intersexual". Digite seu sexo novamente: ')).strip().upper()[0]
while estado_civil not in 'CSVD':
    estado_civil = str(input('Escolha dentre as opções "casada/o", "solteira/o", "viúva/o" ou "divorciada/o". Digite seu sexo novamente: ')).strip().upper()[0]