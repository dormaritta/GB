# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

nums = list(map(int, input('введите числа:').split()))

max_ = 0
min_ = nums[0]

for i in nums[0:]:
    if i > max_:
        max_ = i
    elif i < min_:
        min_ = i
print('минимальное число: ', min_)
print('максимальное число: ', max_)