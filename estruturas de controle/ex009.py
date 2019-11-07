'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal 
e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 0.1)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço 
    parcela = total / 2
    print('Sua conta será parcelada em 2x de R${:.2f}.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 0.2)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua conta será parcelada em {}x de R${:.2f} com juros.'.format(totalparc, parcela))
else: 
    total = 0
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))