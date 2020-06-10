my_dict = {}
sum_hours = ''
with open('text_6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        for el in line:
            if el.isnumeric():
                sum_hours += el
            else:
                sum_hours += ' '
        sum_hours = sum_hours.split()
        for el in range(len(sum_hours)):
            sum_hours[el] = int(sum_hours[el])
        total_hours = sum(sum_hours)
        sum_hours = ''
        tmp_list = line.split()
        my_dict.update({tmp_list[0][:-1]: total_hours})
    print(my_dict)
