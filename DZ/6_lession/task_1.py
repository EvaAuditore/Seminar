# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

def search(list_1):
    search_word = 'qwe'
    count = 0
    for index, value in enumerate(list_1):
        if value == search_word:
            count += 1
            if count == 2:
               print(f'Ищем "{value}", ответ: {index}')

search(list_1)