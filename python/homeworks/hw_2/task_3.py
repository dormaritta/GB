# Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму.

# Пример:

# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

n = int(input("введите число: "))

list = [round((1 + 1/n)**n, 2) for n in range(1, n+1)]

print("последовательность из n чисел:", list)
print("сумма:", round(sum(list), 2))
