# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

coeff = []
k = int(input('какая степень многчлена? '))
for i in range(k+1):
    num = randint(-10, 10)
    coeff.append(num)

print(coeff)

result = ''
for i in range(len(coeff)):
    if len(result) > 0 and coeff[i] > 0:
        result = result + ' + '
    if coeff[i] == 0:
        continue
    result = result + str(coeff[i]) + 'x^' + str(k - i)

if coeff[-1] != 0:
    result = result[:len(result) - 3]

result = result + ' = 0'
print(result)

with open('file.txt', 'w') as f:
    f.write(result)