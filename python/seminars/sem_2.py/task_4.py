# Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой.

# str_1 = input('введите первую строку: ')
# str_2 = input('введите вторую строку: ')
# # print(str_1.count(str_2))


# st = input('введите строку 1: ')
# st2 = input('введите строку 2: ')

st = 'hello, string, hello'
st2 = 'hello'
index = -1
count = 0
while index < len(st):
    index = st.find(st2, index+1)
    if index == -1:
        break
    count += 1
print(count)
