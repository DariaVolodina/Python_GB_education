# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт 
# сумму элементов списка, стоящих 
# на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def SumOfOddElements(list):
#     sum = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             sum += list[i]
#     return sum


# list1 = [1, 100, 2, 200, 1, 444, 3]
# print(list1)
# print(f'Сумма элементов на нечётных позициях списка = {SumOfOddElements(list1)}')

#Вариант с выводом значений элементов на нечётных позициях


# def CreateOddElementsList (list):
#     odd_list = []
#     for i in range(len(list)):
#         if i % 2 != 0:
#             odd_list.append(list[i])
#     return odd_list

# def SumOfElements (list):
#     sum = 0
#     for i in range(len(list)):
#         sum += list[i]
#     return sum


# list1 = [1, 100, 2, 200, 1, 444, 3]
# print(list1)
# new_list = CreateOddElementsList(list1)
# print(f'На нечётных позициях списка элементы {new_list}. Их сумма = {SumOfElements(new_list)}')


#вариант от Марии Андреевой

from random import sample

def list_rand_nums(count: int): #для коллег - так более очевидно. Можно прописать и что получим на выходе
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2): # прописали шаг = 2. для оптимизации
        sum_nums += list_nums[k]
    return sum_nums

all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(sum_odd_pos(all_list))

