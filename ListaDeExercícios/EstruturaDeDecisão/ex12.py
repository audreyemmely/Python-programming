'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00  
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00

'''
valorHora = float(input('Qual o valor da sua hora trabalhada? R$ '))
qtddHoras = float(input('Quantas horas você trabalhou no mês? '))
salárioBruto = valorHora * qtddHoras 

print('\nSalário Bruto: R$ {:.2f}'.format(salárioBruto))

if salárioBruto > 2500:
    IR = salárioBruto*0.2
    print('(-) IR (20%): R$ {:.2f}'.format(IR))
elif salárioBruto > 900 and salárioBruto <= 1500:
    IR = salárioBruto*0.05
    print('(-) IR (5%): R$ {:.2f}'.format(IR))
elif salárioBruto > 1500 and salárioBruto <= 2500:
    IR = salárioBruto*0.1
    print('(-) IR (10%): R$ {:.2f}'.format(IR))
else:
    IR = 0
    print('(-) IR (0%): ISENTO')

INSS = salárioBruto*0.1
FGTS = salárioBruto*0.11
print('(-) INSS (10%): R$ {:.2f}'.format(INSS))
print('FGTS (11%): R$ {:.2f}'.format(FGTS))
total =  IR + INSS + FGTS 
print('Total de descontos: R$ {:.2f}'.format(total))