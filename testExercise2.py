grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))

average = (grade1+grade2)/2

print("Sua média é %.2f" %(average))

if average >= 6:
    print("Aprovado!")
else:
    print("Reprovado.")