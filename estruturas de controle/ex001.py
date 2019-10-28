'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorCasa = float(input('Digite o valor da casa:\nR$ '))
salário = float(input('Digite o seu salário:\nR$ '))
anos = int(input('Quantos anos de financiamento?\n'))
prestação = valorCasa / (anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorCasa, anos, prestação))
if prestação >= (salário*0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')