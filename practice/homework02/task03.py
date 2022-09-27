# Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.


def CreateList(x):
    list = []
    for i in range(1, x + 1):
        x1 = (1 + 1 / i) ** i
        list.append(x1)
    return list

def SumOfElenments(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return round(sum, 2)


n = int(input('Input number of elements in list: '))
list1 = CreateList(n)
print(list1)
print('Sum of elements in this list is', SumOfElenments(list1))
