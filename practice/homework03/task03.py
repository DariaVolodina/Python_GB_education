# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт 
# разницу между максимальным и минимальным 
# значением дробной части элементов.
# минимальное значение дробной части 
# отличное от нуля, у целых чисел дробной 
# части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# вариант от Марии Андреевой

from random import uniform

def list_rand_nums(count: int):
    list_nums = []
    if count <= 0:
        print("Negative value of the number of numbers!")
        return []

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2)) #uniform рандом в заданном диапазоне
    return list_nums


def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)): # нулевое значение уже взяли!
        num = round(list_nums[k] % 1, 2) # берём только дробную часть элемента
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f'Min: {num_min}. Max: {num_max}. Difference: {result}')
    return result

all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(dif_max_min(all_list))



# не работает
# def FractionalPart (list):
#     fract_list = []
#     num = 0
#     for i in range(len(list)):
#         if not list[i] == int(list[i]):
#             num = round(list[i] - int(list[i]), 2)
#             fract_list.append(num)
      
#     return fract_list

# def MaxMinDifference (list):
#     result = 0
#     result = max(list) - min(list)
#     return result

# list1 = [1.1, 1.2, 3.4, 5, 10.01, 7.02]
# print(list1)
# new_list = (FractionalPart(list1))
# print(new_list)
# print(f'Разница между максимальным и минимальным значением дробной части элементов списка равна {MaxMinDifference(new_list)}')




#отдельно выведение мин и макс значений элементов работает НЕКОРРЕКТНО 
# почему...?
# for i in range(len(list)):
    #     max_i = list[0]
    #     min_i = list[0]

        # if list[i] > max_i:
        #     max_i = list[i]
        # if list[i] < min_i:
        #     min_i = list[i]
    # print(max(list))
    # print(min(list))