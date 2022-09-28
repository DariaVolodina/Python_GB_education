# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def SumOfDigits (a):
    str_a = str(a)
    str_a = str_a.replace('.', '')

    int_a = int(str_a)

    result = 0

    while int_a > 0: 
        result += int_a % 10
        int_a //= 10

    return result


# f = 1.234  # ПРОВЕРКА
# print(SumOfDigits(f))

x = float(input('Input real number: '))
print(f'Sum of digits in number {x} is {SumOfDigits(x)}')