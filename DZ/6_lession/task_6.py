# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

num = [(10,25),(3,4),(4,1)]
num_sum =list(map(sum, num))
num_final = [i for i in num_sum if i % 5 == 0]
print(num_final)
