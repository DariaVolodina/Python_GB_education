# Напишите программу, удаляющую из текста 
# все слова, содержащие "абв"

path = 'C:\\Users\\AlexBlues\\Documents\\DEVELOPER\\Python_education\\Python_GB_education\\text.txt'

dataTxt = ''
with open(path, 'r', encoding = 'UTF_8') as file:
    dataTxt = file.read()

print(dataTxt) 

dataTxt = dataTxt.split()
print(dataTxt)

findTxt = input('Input text for check: ')

res_txt = []

for word in dataTxt:
    if findTxt not in word:
        res_txt.append(word)

print(res_txt)