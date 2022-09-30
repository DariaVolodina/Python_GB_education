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


def CreateOddElementsList (list):
    odd_list = []
    for i in range(len(list)):
        if i % 2 != 0:
            odd_list.append(list[i])
    return odd_list

def SumOfElements (list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum


list1 = [1, 100, 2, 200, 1, 444, 3]
print(list1)
new_list = CreateOddElementsList(list1)
print(f'На нечётных позициях списка элементы {new_list}. Их сумма = {SumOfElements(new_list)}')
