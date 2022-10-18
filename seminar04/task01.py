# Задайте строку из набора чисел. 
# Напишите программу, которая покажет 
# большее и меньшее число. В качестве 
# разделителя используйте пробел

# в случае с буквами - некоректные данные

# алгоритм: две фукнкции. 1 - на корректность данных, 
# плюс почистить список
# 2 - используя почищенный список, поиск
# strip чистка

line = input('Input numbers: ')
list_1 = [x.strip(',.!*') for x in line.split() if x.replace('-', '').isdigit()] 
# в COMPREHENSIONS м пишем сначала ЧТО будем делать
# потом С ЧЕМ будем делать
# последний блок - какой фильтр должно проходить значение
# ВСЕГДА будет цикл в comprehensions
# if один, но комбинируется с and, or.... 
# внутри одного компр может лежать еще один. Сложные вложенные структуры.  
# есть list-comprehensions, set-comprehensions & dictionary-comprehensions
# только 3 типа данных поддерживает такой синтаксис

# split убирает все пробелы, все специальные конструкции(\...)
# list(map(int, n)) - сделает список не строковых, а целочисленных значений
# print(*map(int, n))  ЗВЁЗДОЧКА распакует список
# strip чистит список
# здесь replaсе (заменяем минус на "ничего")- временно заменяет, только для проверки число это или нет
print(f'Min: {min(list_1, key = int)}') # ключ, параметр, просим рассматривать строки как ИНТ
print(f'Max: {max(list_1, key = int)}')

#ЕСЛИ РАЗВЕРНУТЬ КОД:
list = []
for x in line.split():
    if x.replace('-', '').isdigit():
        list.append(x.strip(',.!*'))

print(f'Min: {min(list_1, key = int)}') 
print(f'Max: {max(list_1, key = int)}')



# Можно и от первой строки избавиться

# list_1 = [x.strip(',.!*') for x in input().split() if x.replace('-', '').isdigit()] 

# print(f'Min: {min(list_1, key = int)}') 
# print(f'Max: {max(list_1, key = int)}')


def check(str_list):
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace('-', '').isdigit():
            return []
    return str_list

def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    print('The data is incorrect')
    return []

print(*find_max_min(input('Enter the numbers separated by a space: ')))
