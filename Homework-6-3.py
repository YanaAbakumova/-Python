class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    pass

    def get_full_name(self):
        return f'Full name: {self.name + " " + self.surname}'

    def get_total_income(self):
        return f'Total income: {sum(self._income.values())}'


p = Position('Anna', 'Smith', 'manager', {'wage': 100, 'bonus': 20})
print(p.position)
print(p._income)
print(p.get_full_name())
print(p.get_total_income())
