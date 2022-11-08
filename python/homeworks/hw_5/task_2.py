# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def candies(x):
    x = int(
        input(f"{x}, сколько конфет вы возьмете? "))
    while x < 1 or x > 28:
        x = int(
            input("Ошибка! Введите количество конфет, в диапазоне от 1 до 28: "))
    return x

def play():
    player_1 = input("Имя первого игрока: ")
    player_2 = input("Имя второго игрока: ")
    value_candies = 2021
    turn = randint(0, 2)

    if turn:
        print(f"Первым ходит игрок: {player_1}")
    else:
        print(f"Первым ходит игрок: {player_2}")

    while value_candies > 27:
        if turn:
            value_candies -= candies(player_1)
            turn = False
            print(f"На столе осталось: {value_candies} конфет(а)")
        else:
            value_candies -= candies(player_2)
            turn = True
            print(f"На столе осталось: {value_candies} конфет(а)")

    if value_candies:
        print('\n ------------------')
        print(f'{player_1} выиграл(а)!')
        print(' ------------------ \n')
    else:
        print('\n ------------------')
        print(f'{player_2} выиграл(а)!')
        print(' ------------------ \n')
play()