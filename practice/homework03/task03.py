# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт 
# разницу между максимальным и минимальным 
# значением дробной части элементов.
# минимальное значение дробной части 
# отличное от нуля, у целых чисел дробной 
# части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def FractionalPart (list):
    new_list = []
    fract_list = []
    int_list = []
    new_list2 = []

    num = 0
    count = 0
   
    for i in range(len(list)):
        if not list[i] == int(list[i]):
           fract_list.append(list[i])

    print(fract_list)

    for j in range(len(fract_list)):
        num = int(fract_list[j])
        int_list.append(num)

    print(int_list)

    for e in range (len(fract_list)):
        while fract_list[e] != int(fract_list[e]):
            fract_list[e] *= 10
            count += 1
        new_list.append(fract_list[e])  
        print(count)
        new_list2.append(int_list[e] * 10 * count)

    print(new_list)
    print(new_list2)

    # return new_list

list1 = [1.1, 1.2, 3.1, 5, 10.01]
print(list1)
print(FractionalPart(list1))