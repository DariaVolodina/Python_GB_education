# Задайте число. Составьте список чисел негаФибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def fibonacci(n):
#     list_fib =  []
#     for i in range(n): 
#         if i in [0, 1]:
#             list_fib.append(1)
#         else:
#             list_fib.append(list_fib[i - 2] + list_fib[i - 1])
#     return list_fib

# def negafib(list):
#     new_list = []
#     z = len(list) - 1
#     for i in range(len(list)):
#         if i % 2 == 0:
#             new_list.append(list[z - i]) 
#         else:
#             new_list.append(list[z - i] * (-1))
        
#     return new_list



# n = int(input('Input number: '))
# fib = fibonacci(n)
# neg = negafib(fib)
# res = neg + fib
# print(res)


# Вариант от Марии Андреевой

def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i) #иллюзия расширения списка в две стороны
        a, b = b, b + a

    return list_nums

print(*neg_fib(int(input())))