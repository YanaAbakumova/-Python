# способ с "**":
my_func_1 = lambda x, y: x ** y


# способ с циклом:
def my_func_2(x, y):
    """Возвращает число x в степени y

    x - действительное положительное число
    y - целое отрицательное число
    Если пользователь неверно вводит переменные, выводится комментарий к ошибке.
    Переменные запрашиваются до тех пор, пока не будут введены корректно

    """
    if x.count('.') == 1:
        tmp = x.replace('.', '')
    else:
        tmp = x
    while not (tmp.isnumeric() and int(tmp) > 0):
        try:
            if int(tmp) <= 0:
                x = input('Число Х должно быть больше нуля! ')
                if x.count('.') == 1:
                    tmp = x.replace('.', '')
                else:
                    tmp = x
        except ValueError:
            x = input('Х не является числом. Введите действительное положительное число x: ')
            if x.count('.') == 1:
                tmp = x.replace('.', '')
            else:
                tmp = x
    x = float(x)
    while not (y[-1].isnumeric() and y.count('.') == 0 and int(y) < 0):
        if y.count('.') > 0:
            y = input('Число Y должно быть целым! ')
        try:
            if int(y) >= 0:
                y = input('Число Y должно быть меньше нуля! ')
        except ValueError:
            y = input('Y не является числом. Введите целое отрицательное число y: ')
    y = int(y)
    count = 1
    for num in range(1, abs(y) + 1):
        count *= x
    return 1 / count


print(my_func_1(1.1, -2))
print(my_func_2(input('Введите действительное положительное число x '), input('Введите целое отрицательное число y ')))
