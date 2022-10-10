""" Напишите программу, которая на вход принимает 5 чисел 
и находит максимальное из них.

Примеры:
- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90 """

#1

num = [1, 4, 8, 7, 5]
max_ = num[0]

for i in num[1:]:
    if i > max_:
        max_ = i

print(max_)

#2

lst = []
for i in range(5): #пробегает по всем индексам в списке, вместо i+1, +2..
    lst.append(int(input('введите число: '))) #append - добавляет числа в конец списка

max_ = 0
for num in lst:
    if num > max_:
        max_ = num
print(max_)

#3

lst = [5, 15, 20, 345, 10]
print(max(lst))

#4 ввод списка через пробел, любое количество элементов

lst = [int(i) for i in input().split()]
print(lst)




