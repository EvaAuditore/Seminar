# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

numbers = []
number = int(input('Введите число:\n'))
for i in range(number):
    numbers.append(random.randint(-10,10))
print(numbers)

def product_of_numbers(list):
    new_list2 = []
    half_list = len(list)//2
    for i in range(half_list):
        new_list = list[i]*list[len(list)-i-1]
        # new_list2 = []
        new_list2.append(new_list)
    print(new_list2)


product_of_numbers(numbers)
