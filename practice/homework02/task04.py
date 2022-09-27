# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. 

# Позиции хранятся в файле file.txt в одной строке одно число. ... 
# НЕ РАЗОБРАЛАСЬ, где создавать этот файл

def MultElements (array, x, y):
    result = 0

    if x <= len(array) and y <= len(array): 
        i = x - 1
        ii = y - 1
        result = array[i] * array[ii]
        return result

    else: return 'no such a position'



N = int(input('Input number: '))

list = []
for i in range (-N, N + 1):
    list.append(i)
print(list)

a = int(input(f'Input the position of first number from 1 to {len(list)}: ')) 
b = int(input(f'Input the position of first number from 1 to {N * 2 + 1}: ')) 
print(f'Произведение элементов позициях {a} и {b} = {MultElements(list, a, b)}')

