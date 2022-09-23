# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли 
# этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def CheckWeekday(a):
    if a > 5: print("It's weekend")
    else: print('not a weekend')

x = int(input('Input number from 1 to 7: '))

while x < 1 or x > 7: 
    x = int(input('Incorrect number. Try again: '))


CheckWeekday(x)