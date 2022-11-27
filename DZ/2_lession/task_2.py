# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список)
#  чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)


number = int(input('Введите число:\n'))
list_factorial = []
k = 1
for i in range(number):
    i = i + 1
    k = i * k
    # j = print(k)
    list_factorial.append(k)
print(list_factorial)    