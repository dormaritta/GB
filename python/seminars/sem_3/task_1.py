# Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел.

import time


def my_random(min, max):
    time.sleep(0.3)
    return int((time.time() % 1 * (max - min)) + min)


for i in range(10):
    print(my_random(1, 8))

# 2 var

a = 123456

my_list = []
for i in range(10):
    n = a % 100
    my_list.append(n)
    a = (a * 4878454848) % 1000000

print(my_list)
