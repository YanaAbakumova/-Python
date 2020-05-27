# Задание 1
name = input("What is your name? ")
print(f'Hello, {name.capitalize()}')

animal = input('What is your favorite animal? ').lower()
if animal == 'cat':
    print("I like cats too!")
elif animal == 'dog':
    print("I like dogs too!")
else:
    print(f'{animal.capitalize()}. Great!')

age = input('Сколько Вам лет? ')
while not age.isdigit():
    print('Пожалуйста, введите Ваш возраст (число полных лет): ')
    age = input('Сколько Вам лет? ')
if int(age) >= 18:
    print('взрослый')
elif 12 < int(age) < 18:
    print('подросток')
else:
    print('ребенок')
