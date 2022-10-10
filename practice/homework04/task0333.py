# Задайте последовательность цифр. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


def unique_elements_list (s: str):
    ints = []
    new_list = []
    num =  len(s)
    for x in num:
        ints.append(int(x))
    print(num)
    print(ints)
    # for i in range(num):

    #     for j in range(num):
    #         if i != j and list

str_num = '47756688399943'
unique_el = unique_elements_list(str_num)
print(unique_el)