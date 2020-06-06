from sys import argv

script_name, first_par, second_par, third_par = argv


print('Имя скрипта: ', script_name)
print('Выработка в часах: ', first_par)
print('Ставка за час: ', second_par)
print('Премия: ', third_par)
error = 0
for par in argv[1:]:
    try:
        if float(par) < 0:
            print(f'{par} - ошибка! значение должно быть от нуля и выше')
            error = 1
    except ValueError:
        print(f'Ошибка! "{par}" не является числом')
        error = 1
if error == 0:
    print(f'Заработная плата сотрудника - {float(first_par) * float(second_par) + float(third_par)}')
else:
    print('Расчет заработной платы не может быть осуществлен.')
