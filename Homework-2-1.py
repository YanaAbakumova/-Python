# Задание 1
my_list = ['word', 1, 1.1, 1 + 2j, False, [1, 2, 3], (1, 2, 3), {1: 'one', 2: 'two', 3: 'three'}, {1, 2, 3},
           frozenset('word'), None, SyntaxError, bytes(5), bytearray(1)]
for ind, el in enumerate(my_list, 1):
    print(ind, type(el))
