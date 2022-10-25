# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# in  >> 54           9990            650
# out >> [2, 3, 3, 3] [2,3,3,3,5,37]  [2,5,5,13]

# def primeFactor (n):
#     prime = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             prime.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         prime.append(n)
#     return prime

# num = int(input('Input natural number: '))
# print(f'Простые множители числа {num}\n {primeFactor(num)}')

#  от Кирилла:

numbers = int(input('Inout number: '))

devList = []
dev = 2
while numbers > 2:
    if numbers % dev != 0:
        dev += 1
    else:
        numbers //=dev
        devList.append(dev)

print(devList)




