# Задание 5
my_list = [7, 5, 3, 3, 2]
new_rate = int(input('Рейтинг: '))
for el in range(len(my_list)):
    if new_rate > my_list[el]:
        my_list.insert(el, new_rate)
        break
if len(my_list) == 5:
    my_list.append(new_rate)
print(my_list)
