with open("first_file.txt", "w", encoding='utf-8') as file:
    a = 0
    while not a == '':
        a = input('Введите строку для записи: ')
        print(a, file=file)
