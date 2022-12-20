# 2- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

number = int(input('Введите число:\n'))
numbers = [random.randint(-10,10) for i in range(number)]
print(numbers)

def product_of_numbers(list):
    half_list = len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(half_list)]
    print(new_list)

product_of_numbers(numbers)