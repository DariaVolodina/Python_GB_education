# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y # LAMBDA, в строке написано то же, что выше

def mult(x, y):
    return x*y

def calc(op, a, b):
    return (op(a, b))
    # return op(a, b)

print(calc(lambda x, y: x + y, 4, 5))

