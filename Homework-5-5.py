with open('fifth_file.txt', 'w+', encoding='utf-8') as my_file:
    my_file.write('1 2 3.5 -0.5 2 1 1 1 -5.2 -3.8 -33.5')
    my_file.seek(0)
    my_list = my_file.read().split()
    for el in range(len(my_list)):
        my_list[el] = float(my_list[el])
    print(f'Сумма чисел в списке: {sum(my_list)}')
