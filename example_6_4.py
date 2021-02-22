"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police, direction=''):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.speed > 0:
            print('Машина поехала')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self):
        if self.direction == 'left':
            print('Машина повернула налево')
        elif self.direction == 'right':
            print('Машина повернула направо')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction=''):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость {self.speed} км/ч')

    def get_info(self):
        print('Рабочая машина')
        print('Марка:', self.name)
        print('Цвет:', self.color)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction=''):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость {self.speed} км/ч')

    def get_info(self):
        print('Городской автомобиль')
        print('Марка:', self.name)
        print('Цвет:', self.color)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction=''):
        super().__init__(speed, color, name, is_police, direction)

    def get_info(self):
        print('Спорткар')
        print('Марка:', self.name)
        print('Цвет:', self.color)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction=''):
        super().__init__(speed, color, name, is_police, direction)

    def get_info(self):
        print('Полицейская машина')
        print('Марка:', self.name)
        print('Цвет:', self.color)
        if self.is_police:
            print('Зарегистрирована в полиции')
        else:
            print('Эта машина выглядит как полицейская, но в полиции не зарегистрирована')


wc = WorkCar(70, 'black', 'Opel', False)
wc.get_info()
wc.go()
wc.stop()
wc.turn()
wc.show_speed()
print()

tc = TownCar(70, 'red', 'Mazda', False, 'left')
tc.get_info()
tc.go()
tc.stop()
tc.turn()
tc.show_speed()
print()

sc = SportCar(150, 'yellow', 'Ferrari', False, 'right')
sc.get_info()
sc.go()
sc.stop()
sc.turn()
sc.show_speed()
print()

pc = PoliceCar(80, 'black & white', 'BMW', True)
pc.get_info()
pc.go()
pc.stop()
pc.turn()
pc.show_speed()
print()

pc_2 = PoliceCar(100, 'black & white', 'Mercedes', False, 'left')
pc_2.get_info()
pc_2.go()
pc_2.stop()
pc_2.turn()
pc_2.show_speed()
print()

wc_2 = WorkCar(0, 'black', 'Opel', False)
wc_2.get_info()
wc_2.go()
wc_2.stop()
wc_2.turn()
wc_2.show_speed()
print()

print(wc.speed)
print(wc.color)
print(wc.name)
print(wc.is_police)
