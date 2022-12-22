# Реализуйте алгоритм перемешивания списка.
import random
lst = [1,2,3,4,5,6,7,8,9,0]
mix_list = lst.copy()
random.shuffle(mix_list)
print(lst)
print(mix_list)
