from operator import truediv


print('hello world')

value = None
a = 123
b = 1.23
# print(type(a))
# print(type(b))
value = 12345
# print(value)
# print(type(value))

s = "hello \n'world'"
s1 = 'hello "world"'
#print(s) # вывод строки
#print(s1)

#print(a, '-', b, '-', s)
#print('{} - {} - {}'.format(a, b, s))
#print('{2} - {1} - {0}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#list = ["1", "2", "3"]
#col = [, 1, 2, 3, 4.5, True]
#print(list)
#print(col)

#print('Input a')
#a = input()
#print('Input b')
#b = input()
#print(a, b) 

# print('Input a')
# a = int (input()) 
# print('Input b')
# b = int (input())
# print(a, ' + ', b, ' = ', a+b)

print('Input a')
a = float (input()) # вещественные числа  
print('Input b')
b = float (input())
print(a, ' + ', b, ' = ', a+b)

a = int(input('input a: '))
b = int (input('input b: '))
if a > b:
    print(a)
else:
    print(b)

username = input('Input name: ')
if username == 'Mari':
    print('Bingo! Hello, Mari')
elif username == 'Masha':
    print('I was waiting for U, Masha')
elif username == 'John':
    print('John is Number One')
else:
    print('Hello, ', username)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Thats, probable, ')
    print('enough )')
print(inverted)

for i in 1, 2, 3, 4, 5:
    print(i**2)

list = [1, 2, 3, 4, 5]
for i in list:
    print(i**2)

