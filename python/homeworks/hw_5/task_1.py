# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def del_words(string):

    string = tuple(filter(lambda x: "абв" not in x, strg.split()))
    return " " .join(string)

strg = "гуччи флипабв флип флоп!"
result_string = del_words(strg)
print(result_string)