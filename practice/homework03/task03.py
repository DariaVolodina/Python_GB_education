# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт 
# разницу между максимальным и минимальным 
# значением дробной части элементов.
# минимальное значение дробной части 
# отличное от нуля, у целых чисел дробной 
# части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# не работает
def FractionalPart (list):
    fract_list = []
    num = 0
    for i in range(len(list)):
        if not list[i] == int(list[i]):
            num = round(list[i] - int(list[i]), 2)
            fract_list.append(num)
      
    return fract_list

def MaxMinDifference (list):
    result = 0
    result = max(list) - min(list)
    return result

list1 = [1.1, 1.2, 3.4, 5, 10.01, 7.02]
print(list1)
new_list = (FractionalPart(list1))
print(new_list)
print(f'Разница между максимальным и минимальным значением дробной части элементов списка равна {MaxMinDifference(new_list)}')




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