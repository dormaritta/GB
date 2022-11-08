# Создайте программу для игры в "Крестики-нолики".

def PrintList(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            print(b[i][j], end=' ')
        print()


def CheckWins(b):
    if (b[0][0] == 'X' and b[0][1] == 'X' and b[0][2] == 'X' or b[0][0] == '0' and b[0][1] == '0' and b[0][2] == '0' or
        b[1][0] == 'X' and b[1][1] == 'X' and b[1][2] == 'X' or b[1][0] == '0' and b[1][1] == '0' and b[1][2] == '0' or
        b[2][0] == 'X' and b[2][1] == 'X' and b[2][2] == 'X' or b[2][0] == '0' and b[2][1] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][0] == 'X' and b[2][0] == 'X' or b[0][0] == '0' and b[1][0] == '0' and b[2][0] == '0' or
        b[0][1] == 'X' and b[1][1] == 'X' and b[2][1] == 'X' or b[0][1] == '0' and b[1][1] == '0' and b[2][1] == '0' or
        b[0][2] == 'X' and b[1][2] == 'X' and b[2][2] == 'X' or b[0][2] == '0' and b[1][2] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X' or b[0][0] == '0' and b[1][1] == '0' and b[2][2] == '0' or
        b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X' or b[0][2] == '0' and b[1][1] == '0' and b[2][0] == '0'):
        return True
    else:
        return False

a = 3
lst = ['*'] * 3
p = 0
i = 0
j = 0
step = ''
for i in range(a):
    lst[i] = ['*'] * a
PrintList(lst)
for g in range(9):
    if g % 2 == 0:
        step = 'X'
    else:
        step = '0'
    i = int(input('Введите координату по оси "y" (от 1 до 3-х): ')) - 1
    j = int(input('Введите координату по оси "x" (от 1 до 3-х): ')) - 1
    while int(i) < 0 or int(i) > 2 or int(j) < 0 or int(j) > 2 or lst[i][j] != '*':
        print('Ошибка в координатах!')
        i = int(input('Введите координату по оси "y" (от 1 до 3-х): ')) - 1
        j = int(input('Введите координату по оси "x" (от 1 до 3-х): ')) - 1
    lst[i][j] = step
    PrintList(lst)
    CheckWins(lst)
    if CheckWins(lst) == True:
        p = step
        break
if p == 'X':
    print('Победили крестики')
elif p == '0':
    print('Победили нолики')
else:
    print('Ничья!')