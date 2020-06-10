with open('text_3.txt.', 'r', encoding='utf-8') as my_file:
    my_list = my_file.read().split()
    sum_salary = 0
    print('Следующие сотрудники имеют доход менее 20000р: ')
    for el in range(1, len(my_list), 2):
        if float(my_list[el]) < 20000:
            print(my_list[el - 1], '-', my_list[el])
            sum_salary += float(my_list[el])
        else:
            sum_salary += float(my_list[el])
    print(f'Средний доход на сотрудника: {round(sum_salary / (len(my_list) / 2), 2)}')
