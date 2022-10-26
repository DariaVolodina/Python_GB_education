# Напишите программу, удаляющую из текста
# все слова, содержащие "абв".
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample


def createList (n: int):
    list1 = [] # create word from list of symbols
    list_of_words = [] # full list

    for i in range(n):
        for j in range(3):
            list1 = ''.join(sample(['а', 'б', 'в'], k = 3))
        list_of_words.append(list1)

    return list_of_words 
    

def removeSequence (myList: list, s: str):
    for i in myList:
        if s in i:
            myList.remove(i)
    return myList

first_list = createList(int(input('Input number of words: ')))
print(*first_list)

print('\nList with no "абв" sequence:')
print(*removeSequence(first_list, 'абв'))
