# print('hello world')
# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# def Quad (x, y):
#     if x == y ** 2 or y == x ** 2:
#     #     return True
#     # else: False
#         print('yes')
#     else: print('no')

# a = int(input('Input first number: '))
# b = int(input('Input second number: '))
# # print(Quad(a,b))
# Quad(a, b)

# # Вариант2
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# if num1**2 == num2 or num2**2 == num1:
#     print("Yes")
# else:
#     print("No")


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.


# list = []

# #Создаем список в цикле
# for i in range(0, 5):
#     list.append(int(input("Введите число: ")))

# max = list[0]

# #Первый вариант:
# for i in range(1, 5):
#     if list[i] > max:
#         max = list[i]

# print(max)

 
# # #Второй вариант поиска/ В этом варианте нельзя изменять i-й элемент списка 
# for i in list:
#     if i > max:
#         max = i

# print(max)

# #Третий вариант через функции
# def createList(m):
#     list = []
#     for i in range(m):
#         a = int(input(f'Введите x{i + 1}: '))
#         list.append(a)
    
#     return list

# def max_el(array):
    
#     max = 0

#     for i in range(len(array)):
#         if array[i] > array[max]:
#             max = i

#     return array[max]

# b = int(input('Введите количество элементов: '))
# new_array = createList(b)
# max = max_el(new_array)
# print(f'Максимальный элемент: {max}')

# # Вариант другой:
# def array(m):
#     x = []
#     for i in range(m):
#         a = int(input(f'Введите x{i + 1}: '))
#         x.append(a)
    
#     return x

# def max_el(array):
    
#     maxim = 0

#     for i in range(len(array)):
#         if array[i] > array[maxim]:
#             maxim = i

#     return array[maxim]

# l = int(input('Введите количество элементов: '))
# new_array = array(l)
# maxim = max_el(new_array)
# print(f'Максимальный элемент: {maxim}')



# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# a = int(input('Input number: ')) 
# print(list(range(-a, a + 1)))

# def list_of_numbers(x):
#     list = []
#     for i in range(-x, x+1):
#         list.append(i)
#     return list

# number = int(input("Введите число: "))

# x = list_of_numbers(number)

# print(x)

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# num = float(input("Введите число: "))

# part_num = int(num *10 % 10)

# if num % 1 == 0:
#     print("Нет дробной части")
# else:
#     print(part_num)

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

num = int(input("Введите число: "))

if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print("Yes")
else:
    print("No")