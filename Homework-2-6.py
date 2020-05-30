# Задание 6
sum_dict = {'название': [], 'цена': [], 'количество': [], 'eд': []}
structure = []
process = True
while process:
    action = input(
        '1 - Внести новый товар, 2 - Показать список товаров (в структуре каталога), 3 - Показать аналитику, 4 - Выход: ')
    while action != '1' and action != '2' and action != '3' and action != '4':
        action = input('Введите 1(новый товар), 2(список), 3(аналитика) или 4(выход): ')
    if int(action) == 1:
        a = input('Название: ')
        b = input('Цена (руб.коп): ')
        if b.count('.') == 1:
            tmp = b.replace('.', '')
        else:
            tmp = b
        while not (tmp.isnumeric() and int(tmp) > 0):
            b = input('Ошибка в цене! Введите цену в числовом формате (больше нуля): ')
            if b.count('.') == 1:
                tmp = b.replace('.', '')
            else:
                tmp = b
        b = float(b)
        c = input('Количество: ')
        while not (c.isnumeric() and int(c) > 0):
            c = input('Ошибка в количестве! Введите целое число больше нуля: ')
        c = int(c)
        d = input('ед: ')
        structure.append({'название': a, 'цена': b, 'количество': c, 'eд': d})
    if int(action) == 2:
        if len(structure) == 0:
            print('Список пуст')
        else:
            for ind, el in enumerate(structure, 1):
                print((ind, el))
    if int(action) == 3:
        for el in structure:
            for k, v in el.items():
                if v not in sum_dict[k]:
                    sum_dict[k] += [v]
        for k, v in sum_dict.items():
            print(k, v)
    if int(action) == 4:
        print('Процесс завершен')
        process = False
