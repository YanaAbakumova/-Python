import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала.'

    def stop(self):
        return 'Машина остановилась.'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):

        super().__init__(speed, color, name, is_police)
        print(f'Название: {self.name}, Цвет: {self.color}, Скорость: {self.speed}, Полиция? {self.is_police}')
        print(self.go())
        print(self.show_speed())
        print(self.turn(random.choice(['направо', 'налево', 'назад'])))
        print(self.stop())

    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed}! Скорость превышена!'
        else:
            return f'Текущая скорость: {self.speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Название: {self.name}, Цвет: {self.color}, Скорость: {self.speed}, Полиция? {self.is_police}')
        print(self.go())
        print(self.show_speed())
        print(self.turn(random.choice(['направо', 'налево', 'назад'])))
        print(self.stop())

    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed}! Скорость превышена!'
        else:
            return f'Текущая скорость: {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Название: {self.name}, Цвет: {self.color}, Скорость: {self.speed}, Полиция? {self.is_police}')
        print(self.go())
        print(self.show_speed())
        print(self.turn(random.choice(['направо', 'налево', 'назад'])))
        print(self.stop())


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Название: {self.name}, Цвет: {self.color}, Скорость: {self.speed}, Полиция? {self.is_police}')
        print(self.go())
        print(self.show_speed())
        print(self.turn(random.choice(['направо', 'налево', 'назад'])))
        print(self.stop())


tc = TownCar(70, 'yellow', 'towncar', False)
sc = SportCar(120, 'red', 'sportcar', False)
wc = WorkCar(40, 'blue', 'workcar', False)
pc = PoliceCar(90, 'white', 'policecar', True)
