from random import randint
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


# def num_entry(e):
#     value = int(e)
#     return value
#     else: 
#         messagebox.showinfo('Warning!', 'Only digits are accepted')
    # entry.delete(0, tk.END)
    # try:
    #     entry.insert(0, eval(value))
    


def screen3():
    global flag
    frame2.destroy()
    print(flag)

    # count1 = 0
    # count2 = 0  
 
    # while n > max_n:
    if flag:
    # k = num_for_move
        num = tk.Entry(framе3, width=24)
        res = num.get()
        
        print(res)
        print(type(res))
        value = int(res)
        print(value)
        num.pack()

    
        # num.delete(0, tk.END)
        # try:
        #     num.insert(0, '0')
        # except NameError:    
        #     messagebox.showinfo('Warning!', 'Only digits to be accepted.')
        #     num.insert(0, '0')
        
        

        tk.Button(framе3, bg="lavender", text="DONE", activebackground = 'purple').pack(padx=10, pady=10, side=tk.TOP)

        if value < 1 or value > 28:
            messagebox.showinfo('Warning!', 'Possible number 1 ~ 28!')
            num.insert(0, '0')
            

        
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


root.mainloop()
