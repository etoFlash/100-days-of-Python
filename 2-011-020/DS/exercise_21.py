import numpy as np

# Создайте массив , состоящий из 10 случайных целых чисел из диапазона от 1 до 20, затем создайте массив состоящий из
# 10 элементов, начиная с 2. Выведите значения этих массивов, а также их сумму, при помощи функции print()
arr_rand = np.random.randint(1, 21, 10)
arr = np.arange(2, 12)
print(arr_rand)
print(arr)
print(arr_rand + arr)

# Создайте массив , состоящий из 7 случайных целых чисел из диапазона от 0 до 9, затем создайте новый массив состоящий
# из 7 элементов первого массива, увеличенных в 3 раза. Выведите значения этих массивов при помощи функции print()
arr = np.random.randint(0, 10, 7)
arr_new = arr * 3
print(arr)
print(arr_new)

# Создайте массив состоящий из квадратных корней 20 элементов по порядку, начиная с 7. Выведите значение массива
# при помощи функции print()
arr = np.sqrt(np.arange(7, 27))
print(arr)
