# Задайте 2 числа. Напишите программу, которая должна
# находить НОК (наименьшее общее кратное) этих двух чисел

# in 
# >> 17         14          0
# >> 11         18          0

# Out
# >> 187        126         0

from math import gcd
a = int(input('Input first number: '))
b = int(input('Input second number: '))
print(a * b // gcd(a, b))
