class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    pass

    def draw(self):
        return 'Запуск отрисовки Ручкой'


class Pencil(Stationery):
    pass

    def draw(self):
        return 'Запуск отрисовки Карандашом'


class Handle(Stationery):
    pass

    def draw(self):
        return 'Запуск отрисовки Маркером'


s = Stationery('Канцелярская принадлежность')
pen = Pen('Карандаш')
pencil = Pencil('Ручка')
handle = Handle('Маркер')
print(s.title, pen.title, pencil.title, handle.title)
print(s.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
