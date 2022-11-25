import math
# 5- Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

entered_list_a = input('Введите координаты точки A через пробел:').split()
num_list_a = list(map(int, entered_list_a))
print(num_list_a)
entered_list_b = input('Введите координаты точки B через пробел:').split()
num_list_b = list(map(int, entered_list_b))
print(num_list_b)

distance = ((num_list_b[0] - num_list_a[0])**2+(num_list_b[1]-num_list_a[1])**2)**0.5
print(f'Расстояние между точками {num_list_a}{num_list_b} равно {round(distance, 3)}')
