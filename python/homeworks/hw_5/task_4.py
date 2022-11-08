# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    encoding = '' 
    prev_char = '' 
    count = 1

    if not data: return ''
    
    for char in data:
        if char != prev_char:
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

# сжатие

encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE') # значения для сжатия
print(encoded_val) 

# восстановление данных

def rle_encode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decode_val = rle_encode('6A1F2D7C1A17E') # сжатые значения
print(decode_val) 