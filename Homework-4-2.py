import random

first_list = [random.randint(1, 1000) for el in range(1, 16)]
print(f'Исходный список: {first_list}')
print(f'Итоговый список: {[first_list[el] for el in range(1, len(first_list)) if first_list[el] > first_list[el-1]]}')
