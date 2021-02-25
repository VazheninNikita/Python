"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, my_lst):
        self.my_lst = my_lst

    def __add__(self, other):
        result = []
        my_num = []
        for i in range(len(self.my_lst)):
            for j in range(len(self.my_lst[i])):
                my_sum = other.my_lst[i][j] + self.my_lst[i][j]
                my_num.append(my_sum)
                if len(my_num) == len(self.my_lst) + 1:
                    result.append(my_num)
                    my_num = []
        return Matrix(result)

    def __str__(self):
        self.__my_str = ''
        for i in range(len(self.my_lst)):
            for j in range(len(self.my_lst[i])):
                self.__my_str += str(self.my_lst[i][j])
                self.__my_str += ' '
            self.__my_str += '\n'
        return self.__my_str


m_1 = Matrix([[3, 5, 3], [6, 3, 2]])
m_2 = Matrix([[1, 1, 1], [1, 1, 1]])
print(m_1.my_lst)
print(m_1)
print(m_2)
print(m_1 + m_2)
