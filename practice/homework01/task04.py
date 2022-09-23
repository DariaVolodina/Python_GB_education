# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек 
# в этой четверти (x и y).

def Diapason(quarter_num):
    if quarter_num == 1: return ('x > 0, y > 0')
    elif quarter_num == 2: return ('x < 0, y > 0')
    elif quarter_num == 3: return ('x < 0, y < 0')
    elif quarter_num == 4: return ('x > 0, y < 0')
    else: return ('incorrect number of quarter')

a = int(input('Задайте номер четверти: '))
print(f'Диапазон возможных координат точек в {a} четверти: {Diapason(a)}')