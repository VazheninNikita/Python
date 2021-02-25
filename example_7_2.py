"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def measuring(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self._clothes.append(self)

    @property
    def measuring(self):
        pass

    @property
    def total(self):
        # Общий расход ткани на всю одежду
        return sum([item.measuring for item in self._clothes])


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name, size)

    @property
    def measuring(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'{self.name} требует {round(self.size / 6.5 + 0.5, 2)} кв. метра ткани для пошива'


class Suit(Clothes):
    def __init__(self, name, size):
        super().__init__(name, size)

    @property
    def measuring(self):
        return self.size * 2 + 0.3

    def __str__(self):
        return f'{self.name} требует {round(self.size * 2 + 0.3, 2)} кв. метра ткани для пошива'


coat = Coat('Пальто классическое', 7)
suit = Suit('Костюм D&G', 1.73)
print(coat)
print(suit)
print(coat.measuring)
print(suit.measuring)
print(f'Общий расход ткани - {coat.total} кв. метров')
print(f'Общий расход ткани - {suit.total} кв. метров')
