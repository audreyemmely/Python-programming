'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
listagem = ('Borracha', 2, 
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('--'*21)
print('Listagem de preços')
print('--'*21)
for i in listagem:
  if type(i) is str:
    print(f'{i:.<32}', end="")
  else:
    print(f'R$ {i:>6.2f}')
print('--'*21)
