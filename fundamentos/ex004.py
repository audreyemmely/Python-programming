# Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm
valor = float(input('Digite uma distânica em metros:\n'))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000

print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm e {}mm.'.format(valor, km, hm, dam, dm, cm, mm))

