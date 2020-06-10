try:
    with open('text_3.txt', 'r', encoding='utf-8') as my_file:
        print(f'Количество строк в файле = {len(my_file.readlines())}')
        my_file.seek(0)
        for ind, line in enumerate(my_file.readlines(), 1):
            print(f'Количество слов в строке {ind} = {len(line.split())}')
except IOError:
    print('Файла не существует!')
