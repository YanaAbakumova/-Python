my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
with open('text_4.txt', 'r', encoding='utf-8') as read_file:
    with open('fourth_out_file.txt', 'w', encoding='utf-8') as write_file:
        for line in read_file.readlines():
            l = line.split()
            if l[0] in my_dict.keys():
                print(my_dict[l[0]], l[1], l[2], file=write_file)
