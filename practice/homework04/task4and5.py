from random import randint as rI

def createCoef():
    coef = {}
    degree = int(input('Input max degree: '))
    for i in range(degree, -1, -1):
        coef[i] = rI(-20, 20)

    return coef

coefEquation = createCoef()
print(coefEquation)

equation = ''

first = True

for i in coefEquation.items():
    if first: 
        first = False
        if i[1] < 0:
            equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
        elif i[1] > 0:
            equation += str(abs(i[1])) + 'x^' + str(i[0])
    else:
        if i[1] < 0:
            equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
        elif i[1] > 0:
            equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

equation = equation.replace('x^1', 'x').replace('x^0', '').replace(' + ', ' +').replace(' - ', ' -') + ' = 0'

print(equation)

equation = equation.split()

print(equation[:-2])

equation = equation[:-2] # срез списка: убираем два последних элемента

dictEquation = {}

for i in range (len(equation)):
    equation[i] = equation[i].replace('+', '').split('x^')
    dictEquation[int(equation[i][1])] = int(equation[i][0])

print(equation)
print(dictEquation)