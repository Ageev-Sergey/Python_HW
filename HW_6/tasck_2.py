# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random

first_list = [random.randint(-10, 20) for i in range(random.randint(10,15))]
print(first_list)
bool_list = list(map(lambda x: x>5 and x<15, first_list))
print(bool_list)
indexes = [i for i, v in enumerate(first_list) if 5 <= v <= 15]
print("индексы: : ", indexes)



# index_list = []
# for i in first_list:
#     if i > 5 and i < 15:
#         index_list.append(first_list.index(i))
# print(index_list)
