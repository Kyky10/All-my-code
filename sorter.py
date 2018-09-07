from random import randint
my_list = list()
while len(my_list) < 1000:
    a = randint(1, 1000)
    my_list.append(a)
my_list.sort()
print(my_list)
input()
