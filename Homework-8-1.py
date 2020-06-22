class Date:
    def __init__(self, d_m_y):
        self.d_m_y = d_m_y

    @classmethod
    def int_date(cls, d_m_y):
        while True:
            d_m_y = d_m_y.split('-')
            if not len(d_m_y) == 3:
                print('Введите значения через "-".')
                d_m_y = input('Введите число-месяц-год (dd-mm-yyyy): ')
                continue
            elif not len(d_m_y[2]) == 4:
                print('Год должен состоять из 4 цифр.')
                d_m_y = input('Введите число-месяц-год (dd-mm-yyyy): ')
                continue
            try:
                print(*list(map(int, d_m_y)))
                return list(map(int, d_m_y))
            except ValueError:
                print('Неправильный формат даты!')
                d_m_y = input('Введите число-месяц-год (dd-mm-yyyy): ')
                continue

    @staticmethod
    def check_date(d_m_y):
        error = 0
        if d_m_y[2] % 4 == 0 and d_m_y[2] % 100 != 0 or d_m_y[2] % 400 == 0:
            leap_year = True
        else:
            leap_year = False
        if d_m_y[1] in range(1, 8, 2) or d_m_y[1] in range(8, 13, 2):
            if d_m_y[0] <= 31:
                print('Число введено правильно.')
                print('Месяц введен правильно.')
            else:
                print('Число введено неправильно.')
                error += 1
        elif d_m_y[1] in range(4, 7, 2) or d_m_y[1] in range(9, 12, 2):
            if d_m_y[0] <= 30:
                print('Число введено правильно.')
                print('Месяц введен правильно.')
            else:
                print('Число введено неправильно.')
                error += 1
        elif d_m_y[1] == 2:
            if leap_year:
                if d_m_y[0] <= 29:
                    print('Число введено правильно.')
                    print('Месяц введен правильно.')
                else:
                    print('Число введено неправильно.')
                    error += 1
            else:
                if d_m_y[0] <= 28:
                    print('Число введено правильно.')
                    print('Месяц введен правильно.')
                else:
                    print('Число введено неправильно.')
                    error += 1
        else:
            print('Месяц введен неправильно: их всего 12.')
            error += 1
        if error == 0:
            print('Дата введена корректно')
        else:
            print('Дата введена некорректно')

    @classmethod
    def complex_method(cls):
        Date.check_date(Date.int_date(input('Введите число-месяц-год (dd-mm-yyyy): ')))


Date.complex_method()
