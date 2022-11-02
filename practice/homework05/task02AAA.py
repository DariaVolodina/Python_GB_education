# Создайте программу для игры с конфетами 
# человек против человека.

# Правила: На столе лежит 150 конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы 
# забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# ДЛЯ РЕШЕНИЯ ЗАДАЧ 2 и 3 - МОЖНО ИСПОЛЬЗОВАТЬ КОНСОЛЬ 
# или БИБЛИОТЕКУ TKINTER

from random import randint


# intro
player1 = input("Hey there! What's your name?\n")
print(f"-----------------------\nNice to meet U, {player1}. I'm your Computer. Let the game begin!")
player2 = "Computer"

max_n = 28
n = 150
print(f'-----------------------\nSo, we have {n} sweets.\nMaximum for a move is {max_n}. Easy, ha?\n-----------------------')

# first move
print('Let the lot decide...') 
flag = randint(0, 2)
if flag:
    print(f"First moves {player1}")
else:
    print(f"First moves {player2}")


# game
def num_for_move (name):
    x = int(input('You GO! How many sweets U take? '))
    # count = 0
    while x < 1 or x > max_n:
        x = int(input("I bet it was a type miss! Possible number 1 ~ 28! Try again: "))
        # count += 1
    return x
    
def pre_result(name, num, count, all_num):
    print(f"{name} moved. {num} sweets taken. {name} has {count} now. And {all_num} sweets left on the table.\n-----------------------")


count1 = 0 
count2 = 0
while n > max_n:
    if flag:
        k = num_for_move(player1)
        count1 += k
        n -= k
        flag = 0
        pre_result(player1, k, count1, n)
    else:
        k = randint(1, 29)
        count2 += k
        n -= k
        flag = 1
        pre_result(player2, k, count2, n)

if flag:
    print(f"You win! Congratulations, {player1}!")
else:
    print(f"You lose... {player2} eats all the sweets. YAMMY!")


