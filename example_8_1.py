"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    def __init__(self, date_str):
        self.date_str = str(date_str)

    def __str__(self):
        return f'Текущая дата: {self.date_str}'

    @classmethod
    def parser(cls, date_str):
        lst_date = date_str.split('-')
        for i in lst_date:
            print(int(i))

    @staticmethod
    def cntrl_date(date_str):
        lst_date = date_str.split('-')
        if int(lst_date[2]) > 0:
            print('Год указан корректно')
        else:
            print('Год указан неверно')

        if int(lst_date[1]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            print('Месяц указан корректно')
        else:
            print('Месяц указан неверно')

        if int(lst_date[1]) in [1, 3, 5, 7, 8, 10, 12] and int(lst_date[0]) in range(1, 32):
            print('День указан корректно')
        elif int(lst_date[1]) in [4, 6, 9, 11] and int(lst_date[0]) in range(1, 31):
            print('День указан корректно')
        elif int(lst_date[1]) == 2 and int(lst_date[2]) in range(0, 3001, 4) and int(lst_date[0]) in range(1, 30):
            print('День указан корректно')
        elif int(lst_date[1]) == 2 and int(lst_date[2]) not in range(0, 3001, 4) and int(lst_date[0]) in range(1, 29):
            print('День указан корректно')
        else:
            print('День указан неверно')


date_1 = MyDate('31-03-2021')
print(date_1)
MyDate.parser('31-03-2021')

date_2 = MyDate('29-02-2015')
print(date_2)
MyDate.cntrl_date('29-02-2015')

date_3 = MyDate('29-02-2020')
print(date_3)
MyDate.cntrl_date('29-02-2020')
