# Задайте число. Составьте список чисел негаФибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonacci(n):
  list_fib = []

  for f in range(n):
    if f in [1, 2]:
        list_fib.append('1')
    else:
        fib = fibonacci (n + 2) − fibonacci (n + 1)
        list_fib.append(fib)

    return list_fib
 
n = int(input('Input number: '))
print(fibonacci(n))
