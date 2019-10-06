list1 = [2, 23, 1]

#using selection sort
for i in range(len(list1)):
    minimum = i

    for j in range(i+1,len(list1)):
        
        if list1[j] < list1[minimum]:
            minimum = j
    
    if list1[i] != list1[minimum]:
        aux = list1[i]
        list1[i] = list1[minimum]
        list1[minimum] = aux

print(list1) 

#using function
list1.sort()
print(list1)