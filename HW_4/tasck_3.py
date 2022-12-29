# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random
rand_list = [random.randint(0, 10) for i in range(random.randint(10, 15))]
print (rand_list)
unique_numbers = list(set(rand_list))
print(unique_numbers)
