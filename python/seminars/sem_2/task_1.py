# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

from random import randint

n = int(input('введите число: '))

lst = []
for i in range(n):
    num = randint(1, 100)
    lst.append(num)

print(lst)

# or

n = int(input('введите число: '))

lst = []
for i in range(n):
    lst.append(randint(1, 100))

print(lst)
