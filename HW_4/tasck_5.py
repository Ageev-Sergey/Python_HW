# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('HW_4,tasck_5(1).txt', 'r') as data:
    first_polynomial = data.read()

with open('HW_4,tasck_5(2).txt', 'r') as data:
    second_polynomial = data.read()

print(first_polynomial, second_polynomial)


with open('HW_4,tasck_5(Otvet).txt', 'w') as data:
    data.write(f'{first_polynomial} + {second_polynomial}')
