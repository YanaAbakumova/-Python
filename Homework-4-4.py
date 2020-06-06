first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Итоговый список: {[el for el in first_list if first_list.count(el) == 1]}')