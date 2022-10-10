# Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

import datetime
from time import time


def randomN (x):
    list = []
    for i in range(x):
        from datetime import datetime
        t = datetime.now()
        list.append(t)
    return list

n = int(input('print number of elements: '))
print(randomN(n))