# Задание 4
words = input('Введите слова через пробел: ').split(' ')
for i in range(len(words)):
    if len(words[i]) > 10:
        words[i] = words[i][:10]
for ind, el in enumerate(words, 1):
    print(ind, el)
