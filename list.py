my_list = ["abacaxi", "melância", "laranja"]
my_list2 = [1, 2, 3, 4 ,5]
my_list3 = ["morango", 2, 9.89]

print(my_list)
print(my_list2)

for item in my_list3:
    print(item)

#size of list
size = len(my_list)
print(size)

#adding an element 
my_list.append("maracujá")
print(my_list)

#checking if the value is in the list
if 3 in my_list2:
    print("Está na lista!")

#removing an element
del my_list[2:] #[:] to remove all
print(my_list)

#sort
list1 = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
list1.sort()

print(list1)

list2 = ["bola", "abacate", "dinheiro"]
list2.sort()
print(list2)

#sorted
list1 = sorted(list1)
print(list1)

#reverse
list1.reverse()
print(list1)

list2.reverse()
print(list2)

#list comprehension
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]

print("Usando list comprehension")
print(x)
print(y)
print(z)

#enumerate
list3 = ["audrey", "muito", "bonita"]

for i, name in enumerate(list3):
    print(i, name)

#filter
def evenNumbers(i):
    if i%2 == 0:
        return i

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenList = filter(evenNumbers, list4)
print(list(evenList))

#map
def double_func(x):
    return x*2

value = [2, 3, 4, 5, 6]
double_value = map(double_func, value)
print(list(double_value))

#reduce
from functools import reduce

def sum(x, y):
    return x+y

list5 = [1, 3, 5, 10, 20]

sum = reduce(sum, list5)
print(sum)

#zip
my_list4 = [1, 2, 3, 4, 5]
my_list5 = ["audrey", "você", "é", "muito", "legal"]

for number, name in zip(my_list4, my_list5):
    print(number, name)