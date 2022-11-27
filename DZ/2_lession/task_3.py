# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

numbers = []
number = int(input('Введите число:\n'))
for i in range(number):
 numbers.append(random.randint(-100,100))
print(numbers)
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers.insert(i+1,0)
    if numbers[-1] < 0:
        numbers.append(0)
print(numbers)

