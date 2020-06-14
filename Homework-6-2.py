class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self, mass, thickness):
        return self._length * self._width * mass * thickness


rd = Road(100, 10)
print(rd.asphalt(10, 5))
print(rd._width)
print(rd._length)

