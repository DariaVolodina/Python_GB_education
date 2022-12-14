# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# def round_num(n, k):
#     count = 0
#     result = 0
#     while k != int(k):
#         k *= 10
#         count += 1
#     result = round(n, count)
#     return result


# p = 3.14159265359
# # d = float(input('Задайте точность: ')) # для ввода точности пользователем
# d = 0.001
# print(f'Число Пи с точностью {d} = {round_num(p, d)}') 


# то жe с модулем decimal

from decimal import Decimal

def accuracy (n, acc):
    num = Decimal(f'{n}')
    return num.quantize(Decimal(f'{acc}'))

p = 3.14159265359
d = float(input('Задайте точность: ')) 

print(f'Число Пи с точностью {d} = {accuracy(p, d)}') 
