def int_func(word):
    """Принимает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
    Если в слове присутствуют символы, не являющиеся прописными латинскими буквами, ввод запрашивается снова.

    >>> print(int_func('word')) -> 'Word'
    tmp - вспомогательная переменная для подсчета количества маленьких латинских букв, которое должно быть
    равным длине слова

    """
    tmp = len(word)
    for letter in word:
        if not 97 <= ord(letter) <=122:
            print(f'Слово "{word}" содержит символ, не являющийся прописной латинской буквой: "{letter}"')
            tmp = 0
    while not tmp == len(word):
        word = input(f'Исправьте, пожалуйста, слово {word}: ')
        tmp = 0
        for letter in word:
            if not 97 <= ord(letter) <=122:
                print(f'Слово "{word}" содержит символ, не являющийся прописной латинской буквой: "{letter}"')
            else:
                tmp +=1
    return word.title()


string = input('Введите слова: ').split()
new_string = []
for el in string:
    new_string.append(int_func(el))
print(*new_string)
