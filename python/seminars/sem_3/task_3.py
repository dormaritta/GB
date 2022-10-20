# Напишите программу,
# которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
str_find = "йцу"
count = 0

for i in range(len(lst)):
    if str_find == lst[i]:
        count += 1
        if count == 2:
            print(f'значение "{str_find}" встречается {i} раз')

if count < 2:
    print('ничего не найдено')
