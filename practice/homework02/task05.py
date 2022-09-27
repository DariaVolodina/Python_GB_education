# Реализуйте алгоритм перемешивания списка.

# def Shuffle(array):
#     new_list = []

#     import random
#     random.shuffle(array)
#     return array


#  Вариант без функции Shuffle

def Shuffle(array):
    empty_list = []
    import random

    while len(empty_list) != len(array):
        rand_num = random.choice(array)
        if rand_num not in empty_list:
                empty_list.append(rand_num)  
    
    return empty_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list)

print('And if we shuffle the list -> ', Shuffle(list))

