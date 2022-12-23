# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import Fun

lst = Fun.Random_list()
start = 0
finish = len(lst) -1
otvet = []
while start <= finish:
    otvet.append(lst[start]*lst[finish])
    start+=1
    finish-=1
print(lst)
print(otvet)