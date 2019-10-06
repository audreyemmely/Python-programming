#a² + bx + c
#(-b +- sqrt(b² - 4ac))/2
from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
delta_root = sqrt(delta)

x1 = (-b + delta_root)/(2*a)
x2 = (-b - delta_root)/(2*a)

print("x1 = %.2f" %x1)
print("x2 = %.2f" %x2)