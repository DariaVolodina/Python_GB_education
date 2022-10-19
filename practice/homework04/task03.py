# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from random import randrange

def rand_list (n: int):
    if n < 0:
        print('Negative value is unavailable')
        return []

    list1 = []
    for i in range(n):
        list1.append(randrange(n))

    return list1


def unique_elements_list (s: list):
    res_list = []
    my_dict = {}.fromkeys(s, 0) #словарь, состоящий из ключей - ключи уникальны! При этом порядок сохранится. Значения проставляем нули

    for i in s:
        my_dict[i] += 1 # при совпадении элементов увеличиваем счётчик

    for j in my_dict:
        if my_dict[j] == 1:
            res_list.append(j)

    return res_list


# my_list = 47756688399943
my_list = rand_list (int(input('Input number of numbers in list: ')))
print(my_list)
print(unique_elements_list(my_list))
