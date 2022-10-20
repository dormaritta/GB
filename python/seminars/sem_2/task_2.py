# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('введите число: '))

lst = []
for i in range(n):
    lst.append((-3)**i)

print(lst)

# or

n = int(input('введите число: '))

lst = [1]
i = 1
while i < n:
    num = lst[-1] * (-3)  # обращаемся к последнему эл-ту списка
    lst.append(num)
    i += 1

print(lst)

# подсказка по обращению к спискам

# my_list = [3, 6, 3, 1, 7]

# for elem in my_list:
#     print(elem)

# по индексу

# for i in range(len(my_list)):
#     print(my_list[i])
#     my_list[i] = my_list[i] * 2
# print(my_list)
