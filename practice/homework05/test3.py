from curses.ascii import isxdigit
from random import randint
from sys import flags
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry(f'300x300')
root.title('Yammy game')
frame = tk.Frame() 
frame.pack() 
frame2 = tk.Frame()
frame2.pack()
framе3 = tk.Frame()
framе3.pack()


# def press_key(event):
#     print(event.char)
#     if event.char.isdigit():
#         add_digit(event.char)
#     elif event.char in '+-/*':
#         add_operation(event.char)
#     elif event.char == '\r':
#         num_entry()


# root.bind('<Key>', press_key)


# def add_digit(digit):
#     value = calc.get()
#     if value[0] == '0' and len(value) == 1:
#         value = value[1:]
#     # print(value) #проверка
#     num.delete(0, tk.END)
#     num.insert(0, value+digit)


# def add_operation(operation):
#     value = calc.get()
#     if value[-1] in '-+/*':
#         value = value[:-1]
#     calc.delete(0, tk.END)
#     calc.insert(0, value+operation)


def num_entry(entry):
    value = entry.get()
    return value
    # entry.delete(0, tk.END)
    # try:
    #     entry.insert(0, eval(value))
    


def screen3():
    frame2.destroy()
    print(flag)

    # count1 = 0
    # count2 = 0  
 
    # while n > max_n:
    if flag:
    # #         # k = num_for_move
        num = tk.Entry(framе3, width=24)
        num.pack()

        if num < 1 or num > 28:
            messagebox.showinfo('Warning!', 'Possible number 1 ~ 28!')
            num.insert(0, '0')
            
        elif not num.isdigit:
            messagebox.showinfo('Warning!', "No letters! Only digits!")
            num.insert(0, '0')

        k = num_entry(num)
    #         # count1 += k
    #         # n -= k
    #         # flag = 0
            
    # #         # pre_result(player1, k, count1, n)
    else:
        k = randint(1, 29)
            # count2 += k
            # n -= k
            # flag = 1
    #         # pre_result(player2, k, count2, n)
    print(k)
    tk.Button(framе3, bg="lavender", text="DONE", activebackground = 'purple').pack(padx=10, pady=10, side=tk.TOP)




def flag_decision(num_of_players: int):
    flag = randint(0, num_of_players - 1)
    return flag


def first_move():
    tk.Label(frame2, text='Let the lot decide...').pack(padx=10, pady=10, side=tk.TOP)
    if flag:
        tk.Label(frame2, text=f"You go first.").pack(padx=10, pady=10, side=tk.TOP)
    else:
        tk.Label(frame2, text=f"First moves {player2}").pack(padx=10, pady=10, side=tk.TOP)
    tk.Button(frame2, bg="lavender", text="OK", activebackground = 'purple', command=screen3).pack(padx=10, pady=10, side=tk.TOP)
    

def screen2():
    frame.destroy()
    tk.Label(frame2, text=f"So, we have {n} sweets.\nMaximum for a move is {max_n}.\nWho takes the last one - WINS!\nEasy, ha?").pack(padx=10, pady=10, side=tk.TOP)
    tk.Button(frame2, bg="lavender", text="GOT IT", activebackground = 'purple', command=first_move).pack(padx=10, pady=10, side=tk.TOP)



def get_entry():
    player1 = entry_name.get()
    print(player1)
    label = tk.Label(frame, text=f"Nice to meet U, {player1}!\nI'm your Computer.\nLet the game begin!")
    label.pack(padx=10, pady=10, side=tk.TOP)
    tk.Button(frame, text="START", bg = 'violet', command=screen2).pack(padx=10, pady=10, side=tk.TOP)


tk.Label(frame, text="Hey there! What's your name?").pack(padx=10, pady=10, side=tk.TOP)
entry_name = tk.Entry(frame, width=24)
entry_name.pack()
player2 = 'Computer'
# print(player2)
tk.Button(frame, bg="lavender", text="DONE", activebackground = 'purple', command=get_entry).pack(padx=10, pady=10, side=tk.TOP)
max_n = 28
n = 150
number_of_players = 2
flag = flag_decision(number_of_players)
print(flag)









# def press_key(event):
#     print(event.char)
#     if event.char.isdigit():
#         add_digit(event.char)
#     elif event.char in '+-/*':
#         add_operation(event.char)
#     elif event.char == '\r':
#         calculate()


# root.bind('<Key>', press_key)

# def add_digit(digit):
#     value = calc.get()
#     if value[0] == '0' and len(value) == 1:
#         value = value[1:]
#     # print(value) #проверка
#     calc.delete(0, tk.END)
#     calc.insert(0, value+digit)


# def add_operation(operation):
#     value = calc.get()
#     if value[-1] in '-+/*':
#         value = value[:-1]
#     calc.delete(0, tk.END)
#     calc.insert(0, value+operation)


# def clear():
#     calc.delete(0, tk.END)
#     calc.insert(0, '0')


# def make_button(digit):
#     return tk.Button(text=digit, bd=3, font=('Times new Roman', 12), command=lambda: add_digit(digit))


# def operation_button(operation):
#     return tk.Button(text=operation, bd=3, font=('Times new Roman', 12), fg='navy', \
#         command=lambda: add_operation(operation))


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



# def calc_button(operation):
#     return tk.Button(text=operation, bd=3, font=('Times new Roman', 12), fg='tomato', \
#         command=calculate)


# def clear_button(operation):
#     return tk.Button(text=operation, bd=3, font=('Times new Roman', 12), fg='tomato', \
#         command=clear)


# calc = tk.Entry(root, justify=tk.RIGHT, font=('Times new Roman', 14), width=14)
# calc.insert(0, '0')
# calc.grid(row=0, column=0, columnspan=4, stick='wesn', padx=3, pady=3)

# make_button('1').grid(row=1, column=0, stick='wens', padx=3, pady=3)
# make_button('2').grid(row=1, column=1, stick='wens', padx=3, pady=3)
# make_button('3').grid(row=1, column=2, stick='wens', padx=3, pady=3)
# make_button('4').grid(row=2, column=0, stick='wens', padx=3, pady=3)
# make_button('5').grid(row=2, column=1, stick='wens', padx=3, pady=3)
# make_button('6').grid(row=2, column=2, stick='wens', padx=3, pady=3)
# make_button('7').grid(row=3, column=0, stick='wens', padx=3, pady=3)
# make_button('8').grid(row=3, column=1, stick='wens', padx=3, pady=3)
# make_button('9').grid(row=3, column=2, stick='wens', padx=3, pady=3)
# make_button('0').grid(row=4, column=0, stick='wens', padx=3, pady=3)

# operation_button('+').grid(row=1, column=3, stick='wens', padx=3, pady=3)
# operation_button('-').grid(row=2, column=3, stick='wens', padx=3, pady=3)
# operation_button('/').grid(row=3, column=3, stick='wens', padx=3, pady=3)
# operation_button('*').grid(row=4, column=3, stick='wens', padx=3, pady=3)

# calc_button('=').grid(row=4, column=2, stick='wens', padx=3, pady=3)
# clear_button('C').grid(row=4, column=1, stick='wens', padx=3, pady=3)

# root.grid_columnconfigure(0, minsize=60)
# root.grid_columnconfigure(1, minsize=60)
# root.grid_columnconfigure(2, minsize=60)
# root.grid_columnconfigure(3, minsize=60)

# root.grid_rowconfigure(1, minsize=60)
# root.grid_rowconfigure(2, minsize=60)
# root.grid_rowconfigure(3, minsize=60)
# root.grid_rowconfigure(4, minsize=60)


root.mainloop()
