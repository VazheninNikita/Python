"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    def __init__(self):
        self.warehouse = {}

    def to_take(self, name, cnt):
        try:
            self.warehouse[name] = self.warehouse[name] + cnt
        except KeyError:
            self.warehouse[name] = cnt

    def paper_list(self):
        for key, value in self.warehouse.items():
            print(f'{key} - {value} шт.')


class Orgtechnics:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_send(self, wh, cnt):
        wh.to_take(self.name, cnt)


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
p_2 = Printer('Принтер Epson', 11300, 'цветной')
s_1 = Scaner('Сканер Lexmark', 10300, '1920x1080')
c_1 = Copier('Ксерокс Xerox', 23600, 'МФУ')
c_2 = Copier('Ксерокс Xerox', 24300, 'МФУ')
wh = Warehouse()
p_1.to_send(wh, 3)
s_1.to_send(wh, 5)
c_1.to_send(wh, 8)
p_2.to_send(wh, 2)
c_2.to_send(wh, 13)
wh.paper_list()
