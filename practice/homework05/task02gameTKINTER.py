import tkinter as tk
from random import randint
from tkinter import messagebox


def flag_decision(num_of_players: int):
    flag = randint(0, num_of_players - 1)
    return flag


def game(entry, label):
    global count1
    global n

    a = int(entry.get())
    while a < 1 or a > max_n:
        messagebox.showinfo('Warning!', 'Possible number 1 ~ 28!')
        entry.delete(0, tk.END)
        a = int(entry.get())
    count1 += a
    n -= a
    print(f'{n} sweets left')
    print(f'You have {count1} sweets now! Yammy!')
    print(a)
    print(type(a))
    label['text'] = f'aaaa  = {a}'



def mainwindow():
    root = tk.Tk()
    root.geometry(f'250x500+100+100')
    root.title('Yammy game')

    label1 = tk.Label(root, text="Decide how many you'll take for a move.", anchor = 'center')
    label1.grid(row=0, column=0, columnspan= 3, padx=10, pady=10, sticky = 'ew')
    entry1 = tk.Entry(root)
    entry1.grid(row=1, column=0)

    label2 = tk.Label(root, width=24)
    label2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    global count1
    global count2
    global n
    global flag 

    while n > max_n:
        if flag:
            
            # move = ..... Не получается реализовать поочерёдные ходы. Компьютер ходит, пока не останется < 28
            # то есть переменная flag не меняет значение, хотя она глобальная. 

            btn2 = tk.Button(root, bg="lavender", text="DONE", command=lambda: game(entry1, label2))
            btn2.grid(row = 1, column = 2, padx=10, pady=10)

            flag = 0
            print(flag)

        else:
            move = randint(1, 29)
            count2 += move
            n -= move
            flag = 1
            print(f'{n} sweets left')
            print(f"comp took {move}")
            print(flag)

    root.mainloop()


max_n = 28
n = 150
count1 = 0
count2 = 0
number_of_players = 2
flag = flag_decision(number_of_players)
print(flag) #проверка

mainwindow()

