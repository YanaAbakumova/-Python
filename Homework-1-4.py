# Задание 4
number = int(input())
test_number = 0
while number > 0:
    x = number % 10
    if x > test_number:
        test_number = x
    number = number // 10
print(test_number)
