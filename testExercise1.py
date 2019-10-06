age = int(input("Digite a sua idade: "))

if age >= 18:
    print("Parabéns, você já pode ser preso! :)")
elif age > 0 and age < 18:
    print("Você ainda é menor de idade.")
else:
    print("Idade inválida.")