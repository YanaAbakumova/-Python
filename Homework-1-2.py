# Задание 2
n = int(input('Сукунды: '))
hour = n // 60 // 60
if hour < 10:
    hour = '0' + str(hour)
minute = n // 60 % 60
if minute < 10:
    minute = '0' + str(minute)
sec = n % 60
if sec < 10:
    sec = '0' + str(sec)
print(f'{hour}:{minute}:{sec}')
