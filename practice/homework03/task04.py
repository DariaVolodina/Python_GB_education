# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def Binary (x):
#     n = ''
#     while x > 0:
#         a = str(x % 2)
#         n = a + n
#         x //=  2

#     return n

# num = int(input('Input number: '))
# print(f'Число {num} в двоичном отображении = {Binary(num)}')



def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2) # вставить в начало списка
        num //= 2

    print(*list_nums, sep = '') # * РАСПАКОВЫВАЕТ СПИСОК, sep - РАЗДЕЛИТЕЛЬ, ПОЛУЧИТСЯ ИЛЛЮЗИЯ ЧИСЛА

conv_bin(int(input()))

 