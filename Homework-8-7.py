class ComplexNum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return ComplexNum(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        return ComplexNum(self.num1 * other.num1 + self.num2 * -1 * other.num2,
                          self.num1 * other.num2 + self.num2 * other.num1)

    def __str__(self):
        if self.num2 >= 0:
            return f"{round(self.num1, 2)}+{round(self.num2, 2)}j"
        else:
            return f"{round(self.num1, 2)}{round(self.num2, 2)}j"


cn_1 = ComplexNum(135.2, 29)
cn_2 = ComplexNum(18, -43)
print(f'Сложение: {cn_1 + cn_2}')
print(f'Умножение: {cn_1 * cn_2}')

print(f'Проверка умножения: {complex(135.2, 29) * complex(18, -43)}')
