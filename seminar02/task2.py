# 2.	Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Пример:
# o	Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

dict = {}

N = int(input('Input number: '))

for i in range(1, N + 1):
    dict[i] = 3 * i + 1

print(dict)

#вариант через список/// не работает
# def newArray(l):
#     array = []
#     for i in range[l]:
#         x = int(input(f'Input {i + 1} element: '))
#         array.append(x)

#     return array

# array = newArray(5)
# print(array)


# def new_array(l):
#     array = []
#     for i in range(l)


# num = int(input('Input number: '))
# num_list = []

# for i in range(1, num + 1):
#     num_list.append(3 * i + 1)

# print(num_list)