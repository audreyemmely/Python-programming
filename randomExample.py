import random

#random.seed(1) sempre gera o msm resultado
number = random.randint(0, 10)
print(number)

my_list = [6, 45, 9]
number = random.choice(my_list)
print(number)