# захотелось попробовать вызвать сразу 2 исключения: "деление на 0" и "число 10"
class Error1(Exception):
    def __init__(self, txt):
        self.txt = txt


class Error2(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    num_1 = float(input("Введите делимое (число): "))
    num_2 = float(input("Введите делитель (число): "))
    if num_2 == 0:
        raise Error1('Нельзя делить на ноль! ')
    if num_1 == 10 or num_2 == 10:
        raise Error2('Мне не нравится число "10".')
except ValueError:
    print("Вы ввели не число")
except Error1 as err1:
    print(err1)
    try:
        if num_1 == 10 or num_2 == 10:
            raise Error2('Мне не нравится число "10".')
    except Error2 as err2:
        print(err2)
except Error2 as err2:
    print(err2)
else:
    print(f'{num_1} разделить на {num_2} равно {round(num_1 / num_2, 4)}')
