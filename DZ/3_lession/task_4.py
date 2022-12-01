# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите число:\n'))
list = []
while number > 0:
    remainder = number%2
    number = number//2
    list.append(remainder)
    list.reverse()

print(str(list)[1:-1].replace(", ", ""))

