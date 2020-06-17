from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    total_material = 0

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v
        print(f'Размер пальто: {self.v}')
        print(f'Расход ткани на пальто: {self.material()} метров')

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v > 30:
            self.__v = 30
        elif v < 5:
            self.__v = 5
        else:
            self.__v = v

    def material(self):
        Clothes.total_material += round((self.v / 6.5 + 0.5), 2)
        return round((self.v / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h
        print(f'Высота для костюма: {self.h}')
        print(f'Расход ткани на костюм: {self.material()} метров')

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 2.5:
            self.__h = 2.5
        elif h < 0.5:
            self.__h = 0.5
        else:
            self.__h = h

    def material(self):
        Clothes.total_material += round((2 * self.h + 0.3), 2)
        return round((2 * self.h + 0.3), 2)


coat1 = Coat('WinterCoat', 35)
suit1 = Suit('OfficeSuit', 3.3)
print(f'Итого расход материала: {round(Clothes.total_material, 2)}')
suit2 = Suit('NewSuit', 0.4)
print(f'Итого расход материала: {round(Clothes.total_material, 2)}')
coat2 = Coat('NewCoat', 7)
print(f'Итого расход материала: {round(Clothes.total_material, 2)}')