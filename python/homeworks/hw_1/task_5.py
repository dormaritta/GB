# Напишите программу, которая принимает на вход координаты двух
# точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('введите x1: '))
y1 = float(input('введите y1: '))
x2 = float(input('введите x2: '))
y2 = float(input('введите y2: '))

a = x1 - x2
b = y1 - y2

print(int((a**2 + b**2) ** 0.5 * 100) / 100)
