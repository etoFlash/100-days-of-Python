import numpy as np

# Создайте массив , состоящий из 10 случайных целых чисел из диапазона от 1 до 20, затем создайте массив состоящий из 5 элементов, начиная со 2 по порядку. Выведите значения обоих массивов при помощи функции print()

arr_rand = np.random.randint(1, 21, 10)
arr_new = arr_rand[1:6]

print(arr_rand)
print(arr_new)

# Создайте массив , состоящий из 10 случайных целых чисел из диапазона от 0 до 20, затем создайте массив состоящий из элементов, начиная с третьего по порядку до последнего. Выведите значения обоих массивов при помощи функции print()

arr_rand = np.random.randint(0, 21, 10)
arr_new = arr_rand[2:]

print(arr_new)

# Создайте двумерный массив , состоящий из случайных целых чисел из диапазона от 3 до 11, в котором 4 строки и 3 столбца. Затем создайте массив состоящий из элементов , второй и третьей строки и первого и второго столбца по порядку. Выведите значения обоих массивов при помощи функции print()

two_dim_arr = np.random.randint(3, 12, 12).reshape(4, 3)
arr_new = two_dim_arr[1:3, :2]

print(two_dim_arr)
print(arr_new)

# Создайте двумерный массив , состоящий из случайных целых чисел из диапазона от 0 до 9, в котором 4 строки и 6 столбцов. Затем создайте массив состоящий из элементов , которые больше числа 3. Выведите значения обоих массивов при помощи функции print()

two_dim_arr = np.random.randint(0, 10, 24).reshape(4, 6)

arr_new = two_dim_arr[two_dim_arr > 3]

print(two_dim_arr)
print(arr_new)
