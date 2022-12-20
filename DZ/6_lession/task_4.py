# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random
numbers = [random.randint(10,100) for i in range(10)]
print(numbers)
numbers_sum = [sum(map(int, str(element))) for element in numbers]
numbers_final = [i for i in numbers_sum if not i % 2]
print(numbers_final)



