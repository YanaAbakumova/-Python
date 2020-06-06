def fact(n):
    """Находит факториал числа"""
    result = 1
    for el in range(1, n + 1):
        result *= el
    return result

# проверка ввода числа n (целое число больше нуля)
while True:
    try:
        n = int(input('Введите n: '))
        if n > 0:
            break
        else:
            print('Число n должно быть больше нуля!')
            continue
    except ValueError:
        print('Ошибка. Необходимо ввести целое число')
        continue


def fact_list(n):
    """Генерирует список факториалов чисел в диапазоне от 1 до n"""
    for el in range(1, n + 1):
        yield fact(el)


print(fact_list(n))
for el in fact_list(n):
    print(el)
