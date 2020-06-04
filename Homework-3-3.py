def my_func(arg1, arg2, arg3):
    """Находит минимальное число и вычитает его из суммы всех аргументов"""
    min_arg = min(arg1, arg2, arg3)
    return arg1 + arg2 + arg3 - min_arg


print(my_func(5.2, -20.1, 30.5))
