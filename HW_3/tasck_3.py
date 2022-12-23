# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def Random_list():
    N = int(input('введите длину массива N: '))
    lst = []
    for i in range(N):
        lst.append((random.randint(0, 10000))/100)
    return lst


lst = Random_list()
print(lst)

change_lst = []
for i in lst:
    a = int(i)
    change_lst.append(round(i-a, 3))
print(change_lst)
change_lst = sorted(change_lst)
print(change_lst)
otvet = round(change_lst[-1] - change_lst[0], 3)
print(otvet)
