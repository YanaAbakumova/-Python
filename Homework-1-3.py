# Задание 3
n = input()
a = int(n)
if a >= 0:
    b = int(n * 2)
    c = int(n * 3)
else:
    b = -int(str(-a) * 2)
    c = -int(str(-a) * 3)
print(a + b + c)
