# Дан список чисел. Создайте список, в который попадают
# числа, описывающие возрастающую последовательность.
# Порядок чисел менять нельзя. 
# Kirill

import random

list = [x for x in range(1, 10)]
random.shuffle(list)
print(list)

new_list = []

for i in range(len(list) - 1):
    sub_list = [list[i]]
    for k in range(i, len(list) - 1):
        if list[k] < list[k + 1]:
            sub_list.append(list[k + 1])
        else: 
            break
    if len(sub_list) > 1 and ''.join(map(str, sub_list)) not in [''.join(map(str, i)) for i in new_list]: # НЕ РАБОТАЕТ
        new_list.append(sub_list)   

print(new_list)