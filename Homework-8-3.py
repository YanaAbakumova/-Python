class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


output_list = []
while True:
    el = input('Введите элемент списка. Знак "!" завершает ввод: ')
    if el == '!':
        break
    try:
        if el.isalpha():
            raise Error('Неправильный тип элемента списка! Введена строка')
        if type(eval(el)) is int or type(eval(el)) is float:
            output_list.append(float(el))
        else:
            raise Error(f'Неправильный тип элемента списка! Введен {type(eval(el))}')
    except Error as err:
        print(err)
    except SyntaxError:
        print('Неправильный тип элемента списка!')

print(output_list)
