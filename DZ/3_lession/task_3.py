# 3-Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import math
import random

numbers = []
number = int(input('Введите число:\n'))
for i in range(number):
    numbers.append(random.uniform(0, 10))   #подскажите, пжлста, как округлить числа в списке до 2 знаков?
print(numbers)

new_list = []
for i in numbers:
    y = round(i % 1, 2)
    new_list.append(y)
    difference = (max(new_list)-min(new_list))
print(difference)
