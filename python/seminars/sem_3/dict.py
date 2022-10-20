# работа со словарями

a = [1, 3, 5, 6]
a[3] = 8
print(a)

b = {'a': 17, 'b': 22, 'c': 10}
b[3] = 22

my_dict = {
    'dog': 'собака',
    'cat': 'кошка'
}

eng_text = 'dog cat'
rus_text = ''

for word in eng_text.split():
    if word in my_dict:
        rus_text += my_dict[word] + ' '

print(rus_text)

# для n = 6: {1: 4, 2: 7...}

my_dict = {}
n = 6
for i in range(1, n+1):
    my_dict[i] = 3*i + 1

print(my_dict)
