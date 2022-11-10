# Создайте программу для игры с конфетами 
# человек против человека.


from random import randint


# intro
player1 = input("Hey there! What's your name?\n")
print(f"-----------------------\nNice to meet U, {player1}.")
player2 = input("And who's playing against you?\n")
print(f"-----------------------\nNice to meet U, {player1}. Let the game begin!")


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
    x = int(input(f'{name} GOES! How many sweets U take? '))
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
        k = num_for_move(player2)
        count2 += k
        n -= k
        flag = 1
        pre_result(player2, k, count2, n)

if flag:
    print(f"{player1}, you win! Congratulations!")
else:
    print(f"{player2}, you win! Common, eat all your sweets! YAMMY!")


