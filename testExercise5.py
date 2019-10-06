num1 = float(input("Digite o primeiro número: "))
operator = input("Digite o operador: ")
num2 = float(input("Digite o segundo número: "))

#sum
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "*":
    result = num1 * num2
elif operator == "%":
    result = num1 % num2    
elif operator == "**":
    result = num1**num2
else:
    print("Operador inválido!")

print(result)