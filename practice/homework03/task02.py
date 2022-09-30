# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def MultPairsInList (list):
    count = 0
    result = 0
    mult_list = []
    for i in range(len(list)):
        while count != len(list) // 2:
            result = list[i + count] * list[len(list) - 1 - count]
            mult_list.append(result)
            count += 1
    return mult_list
    
list1 = [100, 10, 9, 1, 2, 3]
print(list1)
mult = MultPairsInList(list1)
print(f'Произведения пар чисел списка {mult}')


