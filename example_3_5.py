def my_func():
    """Возвращает сумму чисел, введенных пользователем до ввода спец.символа 'q'."""
    tmp_sum = 0.0
    trgr = ''
    while trgr != 'q':
        tmp_lst = input('Введите числа через пробел: ').split()
        for i in tmp_lst:
            if i != 'q':
                tmp_sum += float(i)
            else:
                trgr = i
                return tmp_sum
        print(tmp_sum)


print(my_func())
