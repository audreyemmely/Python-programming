#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um número:\n'))
print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format(numero*2, numero*3, numero**(1/2)))