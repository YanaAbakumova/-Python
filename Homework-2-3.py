# Задание 3
# dict + list
month = int(input('Месяц: '))
my_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for k, v in my_dict.items():
    if month in v[:]:
        print(k)

# dict
month = int(input('Месяц: '))
my_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
           10: 'осень', 11: 'осень', 12: 'зима'}
print(my_dict.get(month))

# list
month = int(input('Месяц: '))
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month_list.index(month) <= 1 or month_list.index(month) == 11:
    print('зима')
elif 2 <= month_list.index(month) <= 4:
    print('весна')
elif 5 <= month_list.index(month) <= 7:
    print('лето')
else:
    print('осень')
