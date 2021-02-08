def my_func(arg1, arg2, arg3):
    """Возвращает сумму наибольших двух аргументов.

    Позиционные параметры:
    arg1 -- первый аргумент
    arg2 -- второй аргумент
    arg3 -- третий аргумент

    """
    tmp_list = [arg1, arg2, arg3]
    tmp_list.sort(reverse=True)
    return tmp_list[0] + tmp_list[1]


a, b, c = [float(x) for x in input('Введите три числа: ').split()]
print(f'Сумма наибольших двух аргументов = {my_func(a, b, c)}')