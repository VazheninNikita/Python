def int_func(s):
    """Возвращает слово с прописной буквы.

    Позиционные параметры:
    s -- слово из маленьких латинских букв

    """
    return s.capitalize()


my_word = input('Введите слово: ')
print(int_func(my_word))

my_str = input('Введите строку: ').split()
for wrd in my_str:
    print(int_func(wrd), end=' ')
