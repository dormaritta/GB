# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# Примеры:  
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

print('проверка, является ли второе число квадратом первого')

a = int(input('введите первое число: ')) #float, если дробное
b = int(input('введите второе число: '))

if a**2 == b or b**2 == a: #or - либо/или
    print('да')
else:
    print('нет')