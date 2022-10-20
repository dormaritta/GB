# преобразование в двоичную и тд систему(до 16-ной)

a = 14
st = ''
while a > 0:
    ost = a % 2
    st = str(ost) + st
    a = a // 2
print(st)

# or 

a = 14
print(bin(a)[2:])
