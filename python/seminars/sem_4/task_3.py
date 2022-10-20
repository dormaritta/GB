# Задайте два числа.
# Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.

import math

num_1 = int(input('введите число: '))
num_2 = int(input('введите число: '))

i = min(num_1, num_2)

while True:
    if i % num_1 == 0 and i % num_2 == 0:
        break
    i += 1
print(i)

# or

a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
res = math.lcm(a, b)
print('НОК =', res)
