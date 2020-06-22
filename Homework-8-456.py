from abc import ABC, abstractmethod


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.items = {}

    def receive(self, item):
        print(f'Принят товар: {item}')
        self.items.update({item.attr + ' ' + item.name: item.__dict__})
        return self.items

    def send(self):
        department = input('Подразделение (название или номер): ')
        while True:
            obj = input('Введите название товара (например, Printer Canon): ').title()
            if obj not in self.items.keys():
                print('Такого товара нет на складе.')
                continue
            while True:
                qty = input(f'Сколько товаров {obj} отправляем в подразделение? ')
                try:
                    if not qty.isnumeric():
                        raise Error('Введите целое положительное число!: ')
                    qty = int(qty)
                    if self.items[obj]['qty'] >= qty:
                        print(f'Tовар {obj} отправлен в подразделение {department}')
                        self.items[obj]['qty'] -= qty
                        if self.items[obj]['qty'] == 0:
                            print (f'на складе не осталось товара {obj}')
                            self.items.pop(obj)
                        break
                    else:
                        raise Error(f"Недостаточно товаров на складе. Их сейчас {self.items[obj]['qty']} ")
                except Error as err:
                    print(err)
                    continue
            break

    def check_items(self):
        print('Сейчас на складе есть товары: ')
        for ind, (k, v) in enumerate(self.items.items(), 1):
            print(ind, k, v)
        return ''


class Equipment(ABC):
    def __init__(self, name, price, qty, year):
        self.name = name
        self.price = price
        self.qty = qty
        self.year = year

    @abstractmethod
    def show_info(self):
        pass

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year > 2020:
            self.__year = 2020
        elif year < 2010:
            self.__year = 2010
        else:
            self.__year = year


class Printer(Equipment):
    def __init__(self, name, price, qty, year, type):
        self.type = type
        super().__init__(name, price, qty, year)

    attr = "Printer"

    def __str__(self):
        return f'Printer: name {self.name}, price ${self.price}, quantity {self.qty}, year {self.year}, type {self.type}'

    def show_info(self):
        return f'Printer: name {self.name}, price ${self.price}, quantity {self.qty}, year {self.year}, type {self.type}'


class Scanner(Equipment):
    def __init__(self, name, price, qty, year, resolution):
        self.resolution = resolution
        super().__init__(name, price, qty, year)

    attr = "Scanner"

    def __str__(self):
        return f'Scanner: name {self.name}, price ${self.price}, quantity {self.qty}, year {self.year}, resolution {self.resolution} dpi'

    def show_info(self):
        return f'Scanner: name {self.name}, price ${self.price}, quantity {self.qty}, year {self.year}, resolution {self.resolution} dpi'


class Copier(Equipment):
    def __init__(self, name, price, qty, year, two_sided):
        self.two_sided = two_sided
        super().__init__(name, price, qty, year)

    attr = "Copier"

    def __str__(self):
        return f'Copier: name {self.name}, price ${self.price}, quantity {self.qty}, year {self.year}, two_sided? {self.two_sided}'

    def show_info(self):
        return f'Copier: name {self.name}, price ${self.price}, quantity {self.qty}, year {self.year}, two_sided? {self.two_sided}'


p = Printer('Canon', 120, 10, 2008, 'laser')
s = Scanner('Epson', 100.5, 20, 2021, '9600x4800')
c = Copier('Xerox', 150.3, 30, 2017, True)
print(p)
print(s)
print(c)
w = Warehouse()
w.receive(p)
w.receive(s)
w.receive(c)
print(w.check_items())

while True:
    try:
        a = input('1 - Принять новый товар на склад \n 2 - Показать список товаров на складе \n 3 - Отправить товар в подразделение \n 4 - Выход ')
        if int(a) == 1:
            while True:
                b = input(' "p" - Printer, "s" - Scanner, "c" - Copier: ').lower()
                if b == 'p':
                    while True:
                        b = Printer(input('Введите название: ').title(), 100, input('Введите кол-во: '), 2012, 'solid_ink')
                        try:
                            if not b.qty.isnumeric() or int(b.qty) == 0:
                                raise Error('Введите целое положительное число!: ')
                            b.qty = int(b.qty)
                        except Error as err:
                            print(err)
                            continue
                        else:
                            w.receive(b)
                            break
                    break
                elif b == 's':
                    while True:
                        b = Scanner(input('Введите название: ').title(), 98.5, input('Введите кол-во: '), 2018, '4800x4800')
                        try:
                            if not b.qty.isnumeric() or int(b.qty) == 0:
                                raise Error('Введите целое положительное число!: ')
                            b.qty = int(b.qty)
                        except Error as err:
                            print(err)
                            continue
                        else:
                            w.receive(b)
                            break
                    break
                elif b == 'c':
                    while True:
                        b = Copier(input('Введите название: ').title(), 80, input('Введите кол-во: '), 2016, False)
                        try:
                            if not b.qty.isnumeric() or int(b.qty) == 0:
                                raise Error('Введите целое положительное число!: ')
                            b.qty = int(b.qty)
                        except Error as err:
                            print(err)
                            continue
                        else:
                            w.receive(b)
                            break
                    break
                else:
                    print('Ошибка! Введите "p", "s" или "c"')
                    continue
        elif int(a) == 2:
            print(w.check_items())
        elif int(a) == 3:
            w.send()
        elif int(a) == 4:
            break
    except ValueError:
        print('Нужно ввести 1, 2, 3 или 4')
        continue
