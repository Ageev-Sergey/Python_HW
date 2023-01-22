# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

number = 111112222334445
literal = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'


def F_rle(value):
    cof = 1
    rle = []
    value_str = str(value) + '-'
    for i in range(len(value_str)-1):
        x = value_str[i]
        if x == value_str[i+1]:
            if cof == 9:              # добавил разделение 17 на состовляющие (9 и 8), так как 17 по идее должно читаться как "одна семерка"
                rle.append(str(cof))  # Ну как я понял).. или мы должны заранее знать,
                rle.append(x)         # что у нас в строке только символьные значения, и тогда проверять перед символом
                cof = 1               # однозначное, или большее число. Ну или же сохранять RLE как список, список списков, словарь или еще как-то
                continue
            cof += 1
        else:
            rle.append(str(cof))
            rle.append(x)
            cof = 1
    rle = ''.join(rle)
    return rle


def F_is_rle(value):
    de_rle = ""
    value_str = str(value)
    for i in range(1, len(value_str), 2):
        x = int(value_str[i-1])
        while x > 0:
            de_rle += value_str[i]
            x -= 1
    return de_rle


print(F_rle(number))
print(F_rle(literal))

number_rle = F_rle(number)
literal_rle = F_rle(literal)

print(F_is_rle(number_rle))
print(F_is_rle(literal_rle))
