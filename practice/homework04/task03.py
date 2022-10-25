# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# from random import randrange

# def rand_list (n: int):
#     if n < 0:
#         print('Negative value is unavailable')
#         return []

#     list1 = []
#     for i in range(n):
#         list1.append(randrange(n))

#     return list1


# def unique_elements_list (s: list):
#     res_list = []
#     my_dict = {}.fromkeys(s, 0) #словарь, состоящий из ключей - ключи уникальны! При этом порядок сохранится. Значения проставляем нули

#     for i in s:
#         my_dict[i] += 1 # при совпадении элементов увеличиваем счётчик

#     for j in my_dict:
#         if my_dict[j] == 1:
#             res_list.append(j)

#     return res_list


# # my_list = 47756688399943
# my_list = rand_list (int(input('Input number of numbers in list: ')))
# print(my_list)
# print(unique_elements_list(my_list))





# by Kirill

# DICTIONARY
# dict = {1: 'aaa', 2: 'bbbb', 3: 'jjl'}
# dict[4] = 'lklklk'

from random import randint as rI

unique = {} # словарь

myList = ''.join(list(map(str, [rI(0, 9) for i in range(20)])))

print(myList)

for c in myList:
    if unique.get(c):
        unique[c] = unique.get(c) + 1
    else:
        unique[c] = 1

uList = []

for i in unique.items():
    # print(*i) # звёздочка разворачивает кортеж
    if i[1] == 1: # в кортееже 1ый эл-т - это ключ. 2ой эл-т - это значение (value)
        uList.append(i[0])


print(*uList)
