class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Клетка с количеством ячеек: {self.number}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            return 'Невозможно осуществить вычитание!'

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        try:
            return Cell(self.number // other.number)
        except ZeroDivisionError:
            return 'Невозможно осуществить деление на 0!'

    def make_order(self, n):
        return self.number // n * (n * '*' + '\n') + self.number % n * '*'

c1 = Cell(25)
print(c1)
c2 = Cell(3)
print(c2)
print('сложение - ', c1 + c2)
print('вычитание - ', c1 - c2)
print('вычитание - ', c2 - c1)
print('умножение - ', c1 * c2)
print('деление - ', c1 / c2)
c3 = Cell(0)
print('деление - ', c1 / c3)
print(c1.make_order(4))