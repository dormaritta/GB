# Задайте список.
# Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.

num = 123
elem = [123, '234', 123, '567']

def check_number(num, elem):
    for e in elem:
        if e == num:
            return True

if check_number(num, elem):
    print(f'число {num} присутствует в списке')
else:
    print(f'числа {num} в списке нет')

# 2 var

list_ = ['qwe', '2,4', '3', '45']

def is_num(str_):
    if str_.count(',') > 1:
        return False
    elif str_.startswith(','):
        return False

    for i in str_:
        if not i in '0123456789,':
            return False
    return True

for i in list_:
    if is_num(i):
        print(i)
