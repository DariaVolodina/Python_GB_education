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




# Вариант 2:

def float_to_completed_integer(real_number: float) -> int:
    magnitude = int(1)
    temp = float(real_number)
    while not temp.is_integer():
        magnitude *= 10
        temp = real_number * magnitude
    return int(temp)


def get_digits_sum(any_number):
    no_point_number = float_to_completed_integer(any_number)
    no_point_number = abs(no_point_number)
    sum = 0
    while no_point_number > 0:
        sum += no_point_number % 10
        no_point_number //= 10
    return sum
