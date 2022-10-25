# Функция map() применяет указанную функцию 
# к каждому элементу итерируемого объекта
# и возвращает итератор с новыми объектами. 

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x+10, li))
# print(li)


# data = list(map(int, input().split()))
# print(data)


data = list(map(int, '1 2 3 55 777 6'.split()))

for e in data:
    print(e)

print('--')

for e in data:
    print(e)
  
print(data)

