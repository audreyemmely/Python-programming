# -*- coding: utf-8 -*-
print("Hello World!")
print("Olá mundo!")
#-------------------------------------------------------------------------

#math
print(2 + 2)
print(2 * 3)
print(2 ** 3)
print(10 % 3)
#-------------------------------------------------------------------------

#message
message = "Olá mundo"
print (message)
#-------------------------------------------------------------------------

#types
var1 = 1 #integer 
var2 = 1.1 #float
var3 =  "Eu sou demais, heheh" #string
print(var1)
print(var2) 
print(var3)
#-------------------------------------------------------------------------

#comparing
x = 2 
y = 3
print(x == y)
print(x < y)

sum = x + y
print (sum  >= y) 
print (sum < y)
#-------------------------------------------------------------------------

#conditional
print(x == y and x == sum)
x = 3
z = 3
print(x == y and x == z)
print(x == y or x == z)
#-------------------------------------------------------------------------

#if
b = 1 
c = 1000
if b > c:
    print("b é maior que c")
if c > b:
    print("c é maior que b")
#-------------------------------------------------------------------------

#else
d = 1
e = 2

if d > e:
    print("d maior que e")
else:
    print("d não é maior que e")
#-------------------------------------------------------------------------

#elif
f = 1
g = 2
if f == g:
    print("números iguais")
elif g > f:
    print("g maior que f")
else:
    print("números diferentes")
#-------------------------------------------------------------------------

#while
var_1 = 1

while var_1 < 10:
    print(var_1)
    var_1 += 2 #var_1 = var_1 + 2
#-------------------------------------------------------------------------

#for
list1 = [1, 2, 3, 4, 5]
list2 = ["olá", "mundo"]
list3 = [0, "olá", 9.99]
for i in list1:
    print(i)
for i in list2:
    print(i)
for i in list3:
    print(i)
#-------------------------------------------------------------------------

#for/range
for i in range(10):
    print(i)
for i in range(10, 20):
    print(i)
for i in range(10, 20, 2):
    print(i)
#-------------------------------------------------------------------------

#input
number = input("Digite um número: ")
print("O número digitado é: ")
print(number)

name = input("Digite seu nome: ")
print("Bem vindo/a, " + name)
#-------------------------------------------------------------------------

#string
string1 = "Audrey"
string2 = "Emmely"

concatenate = string1 + " " + string2
print(concatenate)

size = len(concatenate)
print(size)

print(string1[2])
print(string1[0:6])

my_string = "O rato roeu a roupa do rei de Roma"
my_list = my_string.split(" ")
print(my_list)

search = my_string.find("rei")
print(search)
print(my_string[search:])

my_string = my_string.replace("o rei", "a rainha")
print(my_string)
#-------------------------------------------------------------------------

#functions
def sumValue(val1, val2):
    print(val1+val2)

sumValue(2, 3)

def mult(val3, val4):
    return val3*val4

m = mult(3, 4)
print(m)