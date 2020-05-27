# Задание 5
revenue = float(input('Выручка: '))
expenses = float(input('Издержки: '))
income = revenue - expenses
if income == 0:
    print('Предприятие работает "в ноль"')
elif income < 0:
    print('Убыток')
else:
    print('Прибыль')
    ros = income / revenue
    print(f'Рентабельность выручки: {ros}')
    employees = int(input('Количество сотрудников: '))
    nipe = income / employees
    print(f'Прибыль на сотрудника: {nipe}')
