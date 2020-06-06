from functools import reduce

multiply = lambda x, y: x * y
print(f'Произведение: {reduce(multiply, [el for el in range(100, 1001) if el % 2 == 0])}')
