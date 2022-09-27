# Напишите программу, которая принимает на вход число
#  N и выдаёт последовательность из N членов.
# Пример:
# o	Для N = 5: 1, -3, 9, -27, 81

def Degree (x):
    list1 = []

    for i in range(0, x):
        list1.append((-3) ** i)
    return list1
     
#     for i in range(0, x):
#         print((-3) ** i, end = ' ')

n = int(input('Input number: '))
array = Degree (n)
print (array)


# -------------------------------------- 1 вариант

# num = int(input('Input number: '))
# result = 1

# for i in range(num):
#     print(result, end = " ")
#     result *= -3


# -------------------------------------- 2 вариант

# num = int(input())

# for i in range(num):
#     print((-3) ** i, end=", ")