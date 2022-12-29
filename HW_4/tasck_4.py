# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Введите показатель степени: "))
polynomial = ''
while k > 0:
    if k == 1:
        polynomial += (f'{random.randint(0,100)}*x**{k}')
        k -= 1
    else:
        polynomial += (f'{random.randint(0,100)}*x**{k} + ')
        k -= 1
print (polynomial)

with open('HW_4,tasck_4.txt', 'w') as data:
    data.write(polynomial)
