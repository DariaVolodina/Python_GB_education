# Реализуйте RLE алгоритм: реализуйте модуль сжатия и 
# восстановления данных. Входные и выходные данные 
# хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c 
# => aaaaaaaaaaabbbccccccc


def rle(s: str):
    result = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        result += str(count) + s[i]
        i += 1

    return result
 

# проверка работы метода:
# x = 'AAAABBCDDDD'
# print(rle(x))

path1 = 'C:\\Users\\AlexBlues\\Documents\\DEVELOPER\\Python_education\\Python_GB_education\\practice\\homework05\\txt1.txt'
path2 = 'C:\\Users\\AlexBlues\\Documents\\DEVELOPER\\Python_education\\Python_GB_education\\practice\\homework05\\txt2.txt'

with open(path1, 'r', encoding='utf-8') as my_f, open(path2, 'w', encoding='utf-8') as encoded_f:
    for line in my_f:
        res = rle(line)
        encoded_f.write(res)
