# Создайте список из N натуральных чисел.
# среди чисел не хватает одного, чтобы выполнить
# условие A[i] - 1 = A[i-1]. Найдите это число

# in >> 10
# out >> [0,1,2,3,4,5,6,7,8,10] >> 9

# in >> 10 
# out >> [1,2,3,4,5,6,7,8,9,10] >> -1

#Kirill

# from random import randint

# list = [x for x in range(10)]
# print(list)

# list.pop(randint(1, len(list) - 1))
# print(list)

# for i in range(1, len(list)):
#     if list[i] - 1 != list[i-1]:
#         print(i)

# Maria

from random import choice

def fill_list(count: int):
    my_list = [x for x in range(count + 1)]
    my_list.remove(choice(my_list))

    return my_list

list1 = fill_list(int(input('Input count: ')))
print(list1)

def find(list):
    for i in range(1, len(list)):
        if list[i] - 1 != list[i-1]:
            return list[i] - 1
    return -1

x = find(list1)
print(x)