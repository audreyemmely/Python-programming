'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Qual o seu salário?\n'))
if salario <= 1250:
    aumento = salario*0.15
    print('Seu aumento será de R${:.2f}, seu novo salário será R${:.2f}'.format(aumento, salario+aumento))
else:
    aumento = salario*0.10
    print('Seu aumento será de R${:.2f}, seu novo salário será R${:.2f}'.format(aumento, salario+aumento))