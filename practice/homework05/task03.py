# Создайте программу для игры в 'Крестики-нолики'.

# ДЛЯ РЕШЕНИЯ ЗАДАЧ 2 и 3 - МОЖНО ИСПОЛЬЗОВАТЬ КОНСОЛЬ
# или БИБЛИОТЕКУ TKINTER

import tkinter as tk
import random


def stop_game():
    global buttons_left
    for item in buttons_left:
        buttons_list[item].config(bg='seashell', state='disabled')


def winner(symbol):
    global game
    if game[0] == symbol and game[1] == symbol and game[2] == symbol \
        or game[3] == symbol and game[4] == symbol and game[5] == symbol \
            or game[6] == symbol and game[7] == symbol and game[8] == symbol \
                or game[0] == symbol and game[3] == symbol and game[6] == symbol \
                    or game[1] == symbol and game[4] == symbol and game[7] == symbol \
                        or game[2] == symbol and game[5] == symbol and game[8] == symbol \
                            or game[0] == symbol and game[4] == symbol and game[8] == symbol \
                                or game[2] == symbol and game[4] == symbol and game[6] == symbol:
        return True


def press_button(a):
    global game
    global buttons_left
    global count
    game[a] = 'X'
    buttons_list[a].config(text='X', bg='seashell2', state='disabled')
    buttons_left.remove(a)

    if a == 4 and count == 0: 
        comp_move = random.choice(buttons_left)
    elif a != 4 and count == 0:
        comp_move = 4
    if count > 0:
        comp_move = 8 - a
    if comp_move not in buttons_left:
        try:
            comp_move = random.choice(buttons_left)
        except:
            label['text'] = 'GAME OVER'

    game[comp_move] = 'O'
    buttons_list[comp_move].config(text='O', bg='seashell2', state='disabled')
    
    if winner("X"): #проверка выигрыша
        label ['text'] = 'You WIN!'
        stop_game()
    elif winner('O'):
        label ['text'] = 'You LOSE!'
        stop_game()
    else:
        if len(buttons_left) > 1: 
            buttons_left.remove(comp_move)
        else:
            label['text'] = 'GAME OVER'
            stop_game()
        print(buttons_left) #проверка - вывод в консоль пустых ячеек
        count += 1
    

game = [i for i in range(9)]
print(game)
buttons_left = list(range(9))
count = 0

root = tk.Tk()
root.title("Tic-tac-toe")
root['bg']='seashell2'
label = tk.Label(width=24, text="Let's play tic-tac-toe", font=('Arial', 12, 'bold'), bg='seashell2')

buttons_list = [tk.Button(width=5, height=2, font=('Arial', 20, 'bold'), bg='medium aquamarine', \
    command=lambda x=i: press_button(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)
buttons_list[0].grid(row=1, column=0, padx=5, pady=5)
buttons_list[1].grid(row=1, column=1, padx=5, pady=5)
buttons_list[2].grid(row=1, column=2, padx=5, pady=5)
buttons_list[3].grid(row=2, column=0, padx=5, pady=5)
buttons_list[4].grid(row=2, column=1, padx=5, pady=5)
buttons_list[5].grid(row=2, column=2, padx=5, pady=5)
buttons_list[6].grid(row=3, column=0, padx=5, pady=5)
buttons_list[7].grid(row=3, column=1, padx=5, pady=5)
buttons_list[8].grid(row=3, column=2, padx=5, pady=5)


root.mainloop()