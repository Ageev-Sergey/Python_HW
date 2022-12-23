# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


a = 1024
b = bin(a)
print(b)

def binn(a):
    otvet = ";)"
    if a % 2 == 0:
        otvet = otvet+"1"
        while a > 1:
            val = a % 2
            if val == 1:
                otvet += "1"
            if val == 0:
                otvet += "0"
            a = a//2
        return otvet
    else:
        while a > 1:
            val = a % 2
            if val == 1:
                otvet += "1"
            if val == 0:
                otvet += "0"
            a = a//2
        otvet = otvet+"1"
        return otvet

d = binn(1024)
print(d)
