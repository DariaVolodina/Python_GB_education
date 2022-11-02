import tkinter as tk
from random import randint
from tkinter import messagebox

root = tk.Tk()
root.geometry('260x260') 
root.title("Yammy game") 
frame = tk.Frame() 
frame.pack() 
frame2 = tk.Frame()
frame2.pack()
framе3 = tk.Frame()
framе3.pack()


# def pre_result(name, num, count, all_num):
#     tk.Label(framе3, text=f"{name} moved.\n{num} sweets taken.\n{name} has {count} now.\nAnd {all_num} sweets left on the table.").pack(padx=10, pady=10, side=tk.TOP) 


def num_for_move():
    # tk.Label(framе3, text="You GO!\nHow many sweets U take?").pack(padx=10, pady=10, side=tk.TOP)
    num = tk.Entry(framе3, width=24)
    num.insert(0, '0')
    num.pack()
    value = num.get()
    # tk.Button(framе3, bg="lavender", text="DONE", activebackground = 'purple', command=next).pack(padx=10, pady=10, side=tk.TOP)
    return value
    # value = int(num.get())
    #     print(x)
    #     count = 0
    #     tk.Button(framе3, bg="lavender", text="DONE", activebackground = 'purple', command=next).pack(padx=10, pady=10, side=tk.TOP)


# def calculate():
#     value = calc.get()
#     calc.delete(0, tk.END)
#     try:
#         calc.insert(0, eval(value))
#     except NameError:
#         messagebox.showinfo('Warning!', 'Only digits to be accepted.')
#         calc.insert(0, '0')
#     except ZeroDivisionError:
#         messagebox.showinfo('Warning!', "Can't divide by zero")
#         calc.insert(0, '0')


        # while x < 1 or x > max_n:
        #     tk.Label(framе3, text="I bet it was a type miss!\nPossible number 1 ~ 28!\nTry again").pack(padx=10, pady=10, side=tk.TOP)
        #     num.delete(0, 'end')    
        #     num = tk.Entry(framе3, width=24)
        #     num.insert(0, "0")
        #     num.pack()
        #     x = int(num.get())
        #     count += 1



# def game ():
#     global n, max_n, framе3, flag, player1
#     frame2.destroy()
#     while n > max_n:
#         if flag:
#             k = num_for_move
#             count1 += k
#             n -= k
#             flag = 0
#             # pre_result(player1, k, count1, n)
#         else:
#             k = randint(1, 29)
#             count2 += k
#             n -= k
#             flag = 1
#             # pre_result(player2, k, count2, n)
    

def next():
    framе3.destroy()



def first_move():
    tk.Label(frame2, text='Let the lot decide...').pack(padx=10, pady=10, side=tk.TOP)
    flag = randint(0, 2)
    if flag:
        tk.Label(frame2, text=f"You go first.").pack(padx=10, pady=10, side=tk.TOP)
    else:
        tk.Label(frame2, text=f"First moves {player2}").pack(padx=10, pady=10, side=tk.TOP)
    tk.Button(frame2, bg="lavender", text="OK", activebackground = 'purple', command=frame2.destroy).pack(padx=10, pady=10, side=tk.TOP)
    global n, max_n
    count1 = 0
    count2 = 0    
    while n > max_n:
        if flag:
            k = 0
            num = 0
            # k = num_for_move
            num = tk.Entry(framе3, width=24)
            num.pack()
            k = int(num.get())
            count1 += k
            n -= k
            flag = 0
            # pre_result(player1, k, count1, n)
        else:
            k = randint(1, 29)
            count2 += k
            n -= k
            flag = 1
            # pre_result(player2, k, count2, n)
    #ход игры
    # max_n = 28
    # n = 150
    # count1 = 0 
    # count2 = 0
    # 

# if flag:
#     print(f"You win! Congratulations, {player1}!")
# else:
#     print(f"You lose... {player2} eats all the sweets. YAMMY!")    



def screen2():
    frame.destroy()
    tk.Label(frame2, text=f"So, we have 150 sweets.\nMaximum for a move is 28.\nWho takes the last one - WINS!\nEasy, ha?").pack(padx=10, pady=10, side=tk.TOP)
    tk.Button(frame2, bg="lavender", text="GOT IT", activebackground = 'purple', command=first_move).pack(padx=10, pady=10, side=tk.TOP)


def get_entry():
    player1 = name.get()
    label = tk.Label(frame, text=f"Nice to meet U, {player1}!\nI'm your Computer.\nLet the game begin!")
    label.pack(padx=10, pady=10, side=tk.TOP)
    tk.Button(frame, text="START", bg = 'violet', command=screen2).pack(padx=10, pady=10, side=tk.TOP)


tk.Label(frame, text="Hey there! What's your name?").pack(padx=10, pady=10, side=tk.TOP)
name = tk.Entry(frame, width=24)
name.pack()
player1 = name.get()
# print(name)
# print(player1)
player2 = 'Computer'
tk.Button(frame, bg="lavender", text="DONE", activebackground = 'purple', command=get_entry).pack(padx=10, pady=10, side=tk.TOP)
max_n = 28
n = 150


root.mainloop()