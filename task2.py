# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def find_pos(lst, string):
    string = str(string)
    i = 0
    count = 0
    while i < len(lst):
        if lst[i] == string:
            count += 1

        if count == 2:
            return i

        i += 1

    return None

sources = [["qwe", "asd", "zxc", "qwe", "ertqwe"],
["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],
["йцу", "фыв", "ячс", "цук", "йцукен"],
["123", "234", 123, "567"],
[]]

search_patterns = ['qwe','йцу','йцу','123','123']

positions = [find_pos(sources[i], search_patterns[i]) for i in range(len(sources))]

for i in range(len(positions)):
	print(sources[i], f'ищем "{search_patterns[i]}"', ' -> ', positions[i])
	
