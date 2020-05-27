# Задание 6
a = float(input('Километры в 1й день: '))
b = float(input('Нужно километров: '))
day = 1
while a < b:
    a = a * 1.1
    day += 1
print(f'Номер дня: {day}')
