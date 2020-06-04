def division(x, y):
    """Принимает делимое и делитель и возвращает их частное.
    Если осуществить деление невозможно, выводится комментарий о причине ошибки, результат не подсчитывается.

    Позиционные параметры:
    x: делимое
    y: делитель

    """
    try:
        float(x) / float(y)
    except ZeroDivisionError:
        if float(y) == 0:
            print('Деление на ноль!')
            return
    except ValueError:
        if x.isalpha() and y.isalpha():
            print('Делимое и делитель не являются числами!')
        elif x.isalpha():
            print('Делимое не является числом!')
        elif y.isalpha():
            print('Делитель не является числом!')
        return
    return float(x) / float(y)


print(division(input('Введите делимое: '), input('Введите делитель: ')))
