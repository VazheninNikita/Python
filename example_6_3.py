"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        print('Полное имя:', self.name, self.surname)

    def get_total_income(self):
        print('Доход:', self._income['wage'] + self._income['bonus'])


p = Position('Никита', 'Важенин', 'Главный специалист', {'wage': 120000, 'bonus': 40000})
p.get_full_name()
p.get_total_income()
print()
print(p.name)
print(p.surname)
print(p.position)
print(p._income)
print()

p = Position('Иванов', 'Иван', 'Ведущий специалист', {'wage': 110000, 'bonus': 20000})
p.get_full_name()
p.get_total_income()
print()
print(p.name)
print(p.surname)
print(p.position)
print(p._income)
