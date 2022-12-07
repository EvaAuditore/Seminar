# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

list_number = [1,1,1,1,2,2,2,3,3,3,4]

def sort_number(list_number):
    list_sort_number = []
    for i in list_number:
        if i not in list_sort_number:
            list_sort_number.append(i)
    print(list_sort_number)

sort_number(list_number)