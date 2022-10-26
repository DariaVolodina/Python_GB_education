# Дан список чисел. Создайте список, 
# в который попадают числа, описывающие 
# возрастающую последовательность.
# Порядок элементов менять нельзя. 

# Мария

from random import choices # нужны дубликаты - лучше choices. Sample не даст дубликатов

def new_list (size: int):
    list_of_numbers = choices(range(1, size * 2), k = size) # choice вернёт список
    return list_of_numbers


my_list = new_list(int(input('Input count: ')))
print(my_list)


def range_nums (list: list):
    my_list = []
    for i in range(len(list)):
        f = list[i]
        list1 = [f]
        for x in range(i+1, len(list)):
            if list[x] > f:
                f = list[x]
                list1.append(f)
        if len(list1) > 1:
            my_list.append(list1)
    return my_list


res_list = range_nums(my_list)
print(res_list)

