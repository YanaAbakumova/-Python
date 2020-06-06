import itertools

# a)
while True:
    try:
        f_num = int(input('Введите первое число списка: '))
        break
    except ValueError:
        print('Ошибка. Необходимо ввести целое число')
        continue
while True:
    try:
        l_num = int(input('Введите последнее число списка: '))
        if l_num > f_num:
            break
        else:
            print('Последнее число должно быть больше первого числа.')
            continue
    except ValueError:
        print('Ошибка. Необъодимо ввести целое число')
        continue
for el in itertools.count(f_num):
    if el > l_num:
        break
    else:
        print(el, end=" ")
print('\n')

# б)
content = input('Введите элементы повторяющегося списка: ')
while True:
    try:
        number = int(input('Сколько раз нужно повторить элементы? '))
        if number >= 0:
            break
        else:
            print('Введите число больше нуля')
            continue
    except ValueError:
        print('Ошибка. Необъодимо ввести целое число')
        continue
stop = 0
for el in itertools.cycle(content):
    if stop == number:
        break
    print(el, end=" ")
    stop += 1
