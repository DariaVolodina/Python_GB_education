# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from random import choice


def poly_sum(name1: str, name2: str):
    with open(name1, 'r', encoding='utf-8') as my_f1, \
            open(name2, 'r', encoding='utf-8') as my_f2:
        first = my_f1.readlines()
        second = my_f2.readlines()

    if len(first) == len(second):
        with open('polynomial_sum.txt', 'a', encoding='utf-8') as my_f3:
            for i, v in enumerate(first): #enumerate возвращает кортеж
                my_f3.write(f'{v[:-5]} + {second[i]}')
            
    else:
        print('The contents of files do not match')


poly_sum('task05_1.txt', 'task05_2.txt')