# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3*n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# dictionary = {
#     'dog': 'собака',
#     'cat': 'кошка'
# }

# # my_dict = dict()
# my_dict2 = {}
# my_dict2[1] = 'Собака'
# my_dict2[1] = 'Собачка'

# print(my_dict2)

n = int(input("введите число: "))

dict = {}
for i in range(1, n + 1):
    dict[i] = 3*i+1
print(dict)

if 7 in dict:
    print(dict[7])
else:
    print('такого элемента не существует')
