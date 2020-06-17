class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        tmp = ''
        for el in self.my_list:
            for i in el:
                tmp += str(i) + ' '
            tmp += '\n'
        return tmp

    def __add__(self, other):
        tmp = []
        # если матрицы разного размера, сначала суммируем элементы попарно, а потом добавляем элементы, оставшиеся "без пары"
        if len(self.my_list) > len(other.my_list):
            for el in range(len(other.my_list)):
                tmp.append([i + j for i, j in zip(self.my_list[el], other.my_list[el])])
                if len(self.my_list[el]) > len(other.my_list[el]):
                    tmp[el].extend(self.my_list[el][len(other.my_list[el]):])
                elif len(other.my_list[el]) > len(self.my_list[el]):
                    tmp[el].extend(other.my_list[el][len(self.my_list[el]):])
            tmp.extend(self.my_list[len(other.my_list):])
        elif len(self.my_list) == len(other.my_list):
            for el in range(len(other.my_list)):
                tmp.append([i + j for i, j in zip(self.my_list[el], other.my_list[el])])
                if len(self.my_list[el]) > len(other.my_list[el]):
                    tmp[el].extend(self.my_list[el][len(other.my_list[el]):])
                elif len(other.my_list[el]) > len(self.my_list[el]):
                    tmp[el].extend(other.my_list[el][len(self.my_list[el]):])
        else:
            for el in range(len(self.my_list)):
                tmp.append([i + j for i, j in zip(self.my_list[el], other.my_list[el])])
                if len(self.my_list[el]) > len(other.my_list[el]):
                    tmp[el].extend(self.my_list[el][len(other.my_list[el]):])
                elif len(other.my_list[el]) > len(self.my_list[el]):
                    tmp[el].extend(other.my_list[el][len(self.my_list[el]):])
            tmp.extend(other.my_list[len(self.my_list):])
        # добавляем нули на пустые позиции, если после сложения разноразмерных матриц кол-во столбцов в итоговой матрице не одинаковое
        max_len = max(len(el) for el in tmp)
        for el in range(len(tmp)):
            if len(tmp[el]) < max_len:
                tmp[el].extend([0 for _ in range(max_len - len(tmp[el]))])
        return Matrix(tmp)


def my_list():
    super_list = []
    while True:
        inner_list = input('Введите целые числа через пробел. Пустая строка завершает матрицу: ').split()
        if inner_list == []:
            break
        else:
            try:
                super_list.append([int(el) for el in inner_list])
            except ValueError:
                print('Ошибка. Необходимо ввести целое число. Введите строку заново.')
                continue
    return super_list


m1 = Matrix(my_list())
print(f'Матрица 1: \n{m1}')
m2 = Matrix(my_list())
print(f'Матрица 2: \n{m2}')
print(f'Cуммарная матрица: \n{m1 + m2}')
