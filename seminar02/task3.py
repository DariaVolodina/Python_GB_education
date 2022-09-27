# 3.	Напишите программу, в которой пользователь будет задавать 
# две строки, а программа - определять количество вхождений 
# одной строки в другой.

# str_first = input('Input text: ')
# str_second = input('Input some more to check: ')

# print(str_first.count(str_second))


str_sub = input('Input fragment: ')
str_src = input('Input text: ')
# sa = 'abc'
# sb = 'abcijojjj abclkjjpjp abckjpoj'

def count (source, substr):
    len_substr = len(substr)
    len_source = len(source)
    i = 0
    for iend in range(len_substr, len_source + 1):
        if source[iend-len_substr:iend] == substr:
            i += 1
    return i

print(f'Число вхожденний строки "{str_sub}" в строку "{str_src}" = ', count(str_src, str_sub))
