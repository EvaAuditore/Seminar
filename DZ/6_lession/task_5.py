# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]
import random
numbers = [random.randint(1,200) for i in range(200)]
print(f'Исходный список: {numbers}')
print(f'Список с индексами:')
print(list(enumerate(numbers)))
numbers_1 = []
for index, value in enumerate(numbers):
    if value != index:
        numbers_1.append(value)
print(f'Итог: {numbers_1}')
print(list(enumerate(numbers_1)))
