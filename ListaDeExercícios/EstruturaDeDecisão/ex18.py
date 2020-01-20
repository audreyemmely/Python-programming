'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

média = (nota1 + nota2 + nota3)/3

if média == 10:
    print('\nAprovado com distinção. Média: %.2f' %média)
elif média >= 7:
    print('\nAprovado. Média: %.2f' %média)
else:
    print('\nReprovado. Média: %.2f' %média)
    