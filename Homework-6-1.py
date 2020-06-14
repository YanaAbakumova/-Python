import time
import turtle

turtle.color("black")
turtle.penup()
turtle.goto(-40, 150)
turtle.pendown()
turtle.forward(80)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(200)
turtle.color("grey")
turtle.penup()
turtle.goto(0, 110)
turtle.pendown()
turtle.dot(45)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.dot(45)
turtle.penup()
turtle.goto(0, -10)
turtle.pendown()
turtle.dot(45)


class TrafficLight:
    count_color = 0

    def __init__(self, color):
        self.__color = color
        TrafficLight.count_color += 1

    def running(self):
        global error
        error = 0
        if self.__color.lower() == 'red':
            if self.count_color == 1 or (self.count_color - 1) % 4 == 0:
                turtle.color("red")
                turtle.penup()
                turtle.goto(0, 110)
                turtle.pendown()
                turtle.dot(45)
                time.sleep(7)
                turtle.color("grey")
                turtle.penup()
                turtle.goto(0, 110)
                turtle.pendown()
                turtle.dot(45)
                return ''
            else:
                error = 1
                return 'Ошибка последовательности цветов!'
        elif self.__color.lower() == 'yellow':
            if self.count_color == 2 or self.count_color % 2 == 0:
                turtle.color("yellow")
                turtle.penup()
                turtle.goto(0, 50)
                turtle.pendown()
                turtle.dot(45)
                time.sleep(2)
                turtle.color("grey")
                turtle.penup()
                turtle.goto(0, 50)
                turtle.pendown()
                turtle.dot(45)
                return ''
            else:
                error = 1
                return 'Ошибка последовательности цветов!'
        elif self.__color.lower() == 'green':
            if self.count_color == 3 or (self.count_color + 1) % 4 == 0:
                turtle.color("green")
                turtle.penup()
                turtle.goto(0, -10)
                turtle.pendown()
                turtle.dot(45)
                time.sleep(5)
                turtle.color("grey")
                turtle.penup()
                turtle.goto(0, -10)
                turtle.pendown()
                turtle.dot(45)
                return ''
            else:
                error = 1
                return 'Ошибка последовательности цветов!'


a = input('Введите последовательность цветов через пробел: ').split()
error = 0
for el in a:
    for i in el:
        if not 97 <= ord(i) <= 122 and not 65 <= ord(i) <= 90:
            el = el.replace(i, '')
    if el.lower() == 'red' or el.lower() == 'yellow' or el.lower() == 'green':
        tl = TrafficLight(el)
        print(tl.running())
    else:
        print('Неправильный цвет!')
        error = 1
    if error == 1:
        break
