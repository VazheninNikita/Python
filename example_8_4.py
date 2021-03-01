"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self):
        self.warehouse = {}


class Orgtechnics:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Orgtechnics):
    def __init__(self, name, price, paint_type):
        super().__init__(name, price)
        self.paint_type = paint_type


class Scaner(Orgtechnics):
    def __init__(self, name, price, scaner_resolution):
        super().__init__(name, price)
        self.scaner_resolution = scaner_resolution


class Copier(Orgtechnics):
    def __init__(self, name, price, copier_type):
        super().__init__(name, price)
        self.copier_type = copier_type


p_1 = Printer('Принтер Epson', 9800, 'цветной')
s_1 = Scaner('Сканер Lexmark', 10300, '1920x1080')
