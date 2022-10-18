# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def MultPairsInList (list):
#     count = 0
#     result = 0
#     mult_list = []
#     for i in range(len(list)):
#         while count != len(list) // 2:
#             result = list[i + count] * list[len(list) - 1 - count]
#             mult_list.append(result)
#             count += 1
#     return mult_list
    
# list1 = [100, 10, 9, 1, 2, 3]
# print(list1)
# mult = MultPairsInList(list1)
# print(f'Произведения пар чисел списка {mult}')

#вариант от Марии Андреевой
from random import sample

def list_rand_nums(count):
    if count < 0:
        print('Negatve value of number of numbers!')
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])
    
    if len_list % 2: # в случае нечетного количества чисел, в конце списка добавится элемент из центра списка
        res_list.append(list_nums[len_list // 2])
    return res_list


all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(prod_pairs(all_list))