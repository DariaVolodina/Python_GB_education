# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Mult_Num (n):
    new_list = []
    for i in range(1, n + 1):
        result = 1
        x = 1
        while x != i + 1:
           result *= x
           x += 1
        new_list.append(result)
        
    return new_list


N = int(input('Input number: '))
print(f'Hабор произведений чисел от 1 до {N} -> {Mult_Num(N)}')