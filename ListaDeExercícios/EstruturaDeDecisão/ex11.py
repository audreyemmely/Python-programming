'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
~ o salário antes do reajuste;
~ o percentual de aumento aplicado;
~ o valor do aumento;
~ o novo salário, após o aumento.
'''
salário = float(input('Digite o seu salário: R$ '))
if salário <= 280:
    reajuste = salário + (salário * 0.2)
    print(' Salário antes do reajuste: R$ {:.2f}\n Percentual de aumento aplicado: 20%\n Valor do aumento: R$ {:.2f}\n Salário após aumento: R$ {:.2f}'.format(salário, salário * 0.2, reajuste))
elif salário > 280 and salário <= 700:
    reajuste = salário + (salário * 0.15)
    print(' Salário antes do reajuste: R$ {:.2f}\n Percentual de aumento aplicado: 15%\n Valor do aumento: R$ {:.2f}\n Salário após aumento: R$ {:.2f}'.format(salário, salário * 0.15, reajuste))
elif salário > 700 and salário <= 1500:
    reajuste = salário + (salário * 0.1)
    print(' Salário antes do reajuste: R$ {:.2f}\n Percentual de aumento aplicado: 10%\n Valor do aumento: R$ {:.2f}\n Salário após aumento: R$ {:.2f}'.format(salário, salário * 0.1, reajuste))
else: 
    reajuste = salário + (salário * 0.05)
    print(' Salário antes do reajuste: R$ {:.2f}\n Percentual de aumento aplicado: 5%\n Valor do aumento: R$ {:.2f}\n Salário após aumento: R$ {:.2f}'.format(salário, salário * 0.05, reajuste))