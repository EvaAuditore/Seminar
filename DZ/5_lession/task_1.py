# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок


text = (input('Введите текст: \n'))
text_exception = input('Введите слово, которое необходимо удалить: \n')

def text_delete(text, text_exception):
    '''
    Функция по удалению слова из текста
    '''
    list_words = text.split(' ')
    new_list_words = []
    for word in list_words:
        if text_exception not in word:
            new_list_words.append(word)
    print(' '.join(new_list_words))
            
text_delete(text, text_exception)



