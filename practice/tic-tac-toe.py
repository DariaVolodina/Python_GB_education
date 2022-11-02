# Создайте программу для игры в 'Крестики-нолики'.

# ДЛЯ РЕШЕНИЯ ЗАДАЧ 2 и 3 - МОЖНО ИСПОЛЬЗОВАТЬ КОНСОЛЬ
# или БИБЛИОТЕКУ TKINTER

import tkinter as tk
from random import randint

window = tk.Tk()
window.title("Tic-tac-toe")
game_cont = True 
field = []
cross_count = 0


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_cont
    game_cont = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_cont and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')

        if game_cont and cross_count < 5:
            bot_move()
            check_win('O')


def check_win(move):
    for n in range(3):
        line_check(field[n][0], field[n][1], field[n][2], move)
        line_check(field[0][n], field[1][n], field[2][n], move)
    line_check(field[0][0], field[1][1], field[2][2], move)
    line_check(field[2][0], field[1][1], field[0][2], move)


def line_check(a, b, c, move):
    if a['text'] == move and b['text'] == move and c['text'] == move:
        a['background'] = b['background'] = c['background'] = 'purple'
        global game_run
        game_run = False


def possible_win(a, b, c, move):
    res = False
    if a['text'] == move and b['text'] == move and c['text'] == ' ':
        c['text'] = 'O'
        res = True
    if a['text'] == move and b['text'] == ' ' and c['text'] == move:
        b['text'] = 'O'
        res = True
    if a['text'] == ' ' and b['text'] == move and c['text'] == move:
        a['text'] = 'O'
        res = True
    return res


def bot_move():
    for n in range(3):
        if possible_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if possible_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if possible_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if possible_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if possible_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if possible_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if possible_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if possible_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = tk.Button(text=' ', width=4, height=2,
                           font=('Times new Roman', 20, 'bold'),
                           background='lavender',
                           command=lambda r=row, c=col: click(r, c))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_btn = tk.Button(text='New game', command=new_game)
new_btn.grid(row=3, column=0, columnspan=3, sticky='nswe') #Виджеты можно растягивать на весь объем ячейки (sticky=N+S+W+E)


window.mainloop()
