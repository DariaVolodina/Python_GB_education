from asyncio import events
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry(f'240x273+100+200')
root['bg'] = 'LavenderBlush2'
root.title('Calculator')


def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


root.bind('<Key>', press_key)

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    # print(value) #проверка
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def make_button(digit):
    return tk.Button(text=digit, bd=3, font=('Times new Roman', 12), command=lambda: add_digit(digit))


def operation_button(operation):
    return tk.Button(text=operation, bd=3, font=('Times new Roman', 12), fg='navy', \
        command=lambda: add_operation(operation))


def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except NameError:
        messagebox.showinfo('Warning!', 'Only digits to be accepted.')
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo('Warning!', "Can't divide by zero")
        calc.insert(0, '0')



def calc_button(operation):
    return tk.Button(text=operation, bd=3, font=('Times new Roman', 12), fg='tomato', \
        command=calculate)


def clear_button(operation):
    return tk.Button(text=operation, bd=3, font=('Times new Roman', 12), fg='tomato', \
        command=clear)


calc = tk.Entry(root, justify=tk.RIGHT, font=('Times new Roman', 14), width=14)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='wesn', padx=3, pady=3)

make_button('1').grid(row=1, column=0, stick='wens', padx=3, pady=3)
make_button('2').grid(row=1, column=1, stick='wens', padx=3, pady=3)
make_button('3').grid(row=1, column=2, stick='wens', padx=3, pady=3)
make_button('4').grid(row=2, column=0, stick='wens', padx=3, pady=3)
make_button('5').grid(row=2, column=1, stick='wens', padx=3, pady=3)
make_button('6').grid(row=2, column=2, stick='wens', padx=3, pady=3)
make_button('7').grid(row=3, column=0, stick='wens', padx=3, pady=3)
make_button('8').grid(row=3, column=1, stick='wens', padx=3, pady=3)
make_button('9').grid(row=3, column=2, stick='wens', padx=3, pady=3)
make_button('0').grid(row=4, column=0, stick='wens', padx=3, pady=3)

operation_button('+').grid(row=1, column=3, stick='wens', padx=3, pady=3)
operation_button('-').grid(row=2, column=3, stick='wens', padx=3, pady=3)
operation_button('/').grid(row=3, column=3, stick='wens', padx=3, pady=3)
operation_button('*').grid(row=4, column=3, stick='wens', padx=3, pady=3)

calc_button('=').grid(row=4, column=2, stick='wens', padx=3, pady=3)
clear_button('C').grid(row=4, column=1, stick='wens', padx=3, pady=3)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)


root.mainloop()
