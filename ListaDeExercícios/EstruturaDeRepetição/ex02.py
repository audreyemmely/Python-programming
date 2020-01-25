'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
while 1:
    nome = str(input('Nome de usuário: ')).strip()
    senha = str(input('Senha: ')).strip()
    if nome != senha:
        break
    print('Tente novamente. A senha precisa ser diferente do nome de usuário.')
print(f'\nVocê fez tudo correto.')