from random import randint
import tkinter as tk
from functools import partial
# from tkinter import *

# from tkinter import messagebox

root = tk.Tk()
root.geometry(f'250x500+100+100')
root.title('Yammy game')

screen1 = tk.Frame()
screen1.pack()

# def num_for_move(entry, label):
#     a = int(entry.get())
#     return (a)
#     print(type(a))
#     label['text'] = f'aaaa  = {a}'

def num_for_move(entry, label):
    global move
    move = int(entry.get())
    label['text'] = f'aaaa  = {move}'
   
# def num_for_move(name):
#     entry1 = tk.Label(screen2, text="Decide how many you'll take for a move.", anchor = 'center').grid(row=0, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
#     num = int(tk.Entry(screen2, width=24).get())
#     num.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
#     tk.Button(screen1, bg="lavender", text="DONE", activebackground = 'purple').grid(row = 1, column = 2, padx=10, pady=10)
#     return num
#     print(num)


def flag_decision(num_of_players: int):
    flag = randint(0, num_of_players - 1)
    return flag


def first_move():
    tk.Label(screen1, text='Let the lot decide...').grid(row=6, column=0,columnspan=3, padx=10, pady=10, sticky = 'ew')
    if flag:
        tk.Label(screen1, text=f"You go first.").grid(row=7, column=0,columnspan=3, padx=10, pady=10, sticky = 'ew')
    else:
        tk.Label(screen1, text=f"First moves {player2}").grid(row=7, column=0,columnspan=3, padx=10, pady=10, sticky = 'ew')

    tk.Button(screen1, bg="lavender", text="OK", activebackground = 'purple', command=screen2)\
        .grid(row=8, column=1, padx=10, pady=10, sticky = 'ew')


def screen2():
    global screen2
    screen1.destroy()
    screen2 = tk.Frame()
    screen2.pack()


def rules_txt():
    tk.Label(screen1, text=f"So, we have {n} sweets.\nMaximum for a move is {max_n}.\nWho takes the last one - WINS!\nEasy, ha?")\
        .grid(row=4, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
    tk.Button(screen1, bg="lavender", text="GOT IT", activebackground = 'purple', \
        command=first_move).grid(row=5, column=1, padx=10, pady=10, sticky = 'ew')


def intro():
    player1 = entry_name.get()
    print(player1) #проверка
    label2 = tk.Label(screen1, text=f"Nice to meet U, {player1}!\nI'm your Computer.\nLet the game begin!", anchor = 'center')\
        .grid(row=2, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
    tk.Button(screen1, text="START", bg = 'violet', command=rules_txt).grid(row=3, column=1, padx=10, pady=10, sticky = 'ew')


label = tk.Label(screen1, text="Hey there! What's your name?", anchor = 'center').grid(row=0, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
entry_name = tk.Entry(screen1, width=24)
entry_name.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


tk.Button(screen1, bg="lavender", text="DONE", activebackground = 'purple', \
    command=intro).grid(row = 1, column = 2, padx=10, pady=10)

player1 = entry_name.get()
player2 = 'Computer'
print(player2) #проверка

max_n = 28
n = 150
number_of_players = 2
flag = flag_decision(number_of_players)
print(flag) #проверка

while n > max_n:
    if flag:
        # move = num_for_move(player1)
        label1 = tk.Label(screen2, text="Decide how many you'll take for a move.", anchor = 'center').grid(row=0, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
        entry1 = tk.Entry(screen2, width=24).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        move = partial(num_for_move, entry1, label1)
        # label2 = tk.Label(screen2, text="Decide how many you'll take for a move.", anchor = 'center').grid(row=0, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
        # entry1 = tk.Entry(screen2, width=24).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        # num = int(entry2.get())
   
        # tk.Button(screen2, bg="lavender", text="DONE", activebackground = 'purple').grid(row = 1, column = 2, padx=10, pady=10)

        # print(num)

        print(move)
        # entry.insert(0, "0")# вставка начальных данных
        # k = int(entry.get())

        # if k < 1 or k > 28:55
        #     messagebox.showinfo('Warning!', 'Possible number 1 ~ 28!')
        #     entry.insert(0, '0')

        # count1 += k
        # n -= move
        flag = 0

    else:
        move = randint(1, 29)
        # count2 += k
        # n -= move
        flag = 1
    # display_preresult
    # print(k)





root.mainloop()