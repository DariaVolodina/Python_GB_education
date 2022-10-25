# LIST COMPREHENSIONS

# [exp for item in iterable]
# [exp for item in iterable(if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

#  Например. Задача: создать список из чётных чисел в диапазоне от 1 до 100

# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

list = [i for i in range(1, 101) if (i % 2 == 0)]

print(list)
print()

# список кортежей
list = [(i, i) for i in range(1, 101) if (i % 2 == 0)]

print(list)
print()

# добавим ещё функцию


def f(x):
    return x**3


list1 = [(i, f(i)) for i in range(1, 21) if (i % 2 == 0)]

print(list1)
print()
