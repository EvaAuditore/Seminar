# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


number = int(input('Введите цифру:\n'))

def prime_number(number):
    list_prime_number = []
    for i in range(2, number):
        if number % i == 0:
             number /= i
             list_prime_number.append(i)
    print(list_prime_number)

prime_number(number)
