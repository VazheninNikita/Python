"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""
from functools import reduce


def multyply_func(a, b):
    """ Возвращает произведение двух элементов

    Позиционные параметры:
    a -- первый множитель
    b -- второй множитель

    """
    return a * b


my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(multyply_func, my_list))
