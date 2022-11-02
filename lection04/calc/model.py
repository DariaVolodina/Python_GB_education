# sum = lambda a, b: a + b

# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {sum(x, y)}')

# Простовата схема
# "АРХИТЕКТУРА приложения", блок-схемы

x = 0
y = 0

def init(a, b): # метоз отвечает за инициализацию = задание начальных значений
    global x
    global y
    x = a
    y = b 

def do_it(): # метод, выполняющие операцию: здесь сложение двух чисел
    return x + y





