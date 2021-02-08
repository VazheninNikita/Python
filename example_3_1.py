def div_func(a, b):
    """Возвращает частное от деления.

    Позиционные параметры:
    a -- делимое
    b -- делитель

    """
    try:
        return (a / b)
    except ZeroDivisionError:
        return ('Деление на 0')


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))

print(div_func(a, b))
