# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

quarter = int(input('Введите цифру, соответствующую номеру четверти:\n'))
if quarter < 0 or quarter > 4:  # Подскажите, пжлста, как указать в этой строке, что нельзя писать текст?
    print('Введите корректное число от 1 до 4')
elif quarter == 1:
    print(
        f'Диапазон возможных координат точек для {quarter} четверти x∈(0, ∞) u y∈(0,∞)')
elif quarter == 2:
    print(
        f'Диапазон возможных координат точек для {quarter} четверти x∈(-∞, 0) u y∈(0,∞)')
elif quarter == 3:
    print(
        f'Диапазон возможных координат точек для {quarter} четверти x∈(-∞, 0) u y∈(-∞, 0)')
elif quarter == 4:
    print(
        f'Диапазон возможных координат точек для {quarter} четверти x∈(0, ∞) u y∈(-∞, 0)')