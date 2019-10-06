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
