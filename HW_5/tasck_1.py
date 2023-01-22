# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв".


line = 'ячсабвнгш йцукенгвба фывабвйцу кенабвджэ'
arr = line.split()
print(arr)

for i in reversed(arr):
    if 'абв' in i:
        arr.remove(i)
arr = " ".join(arr)
print(arr)
