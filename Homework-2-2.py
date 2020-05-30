# Задание 2
input_list = input('Введите элементы списка через пробел: ').split()
output_list = []
pairs = (len(input_list)) // 2
i = 1
for num in range(pairs):
    output_list.append(input_list[num+i])
    output_list.append(input_list[num+i-1])
    i += 1
if len(input_list) % 2 != 0:
    output_list.append(input_list[-1])
print(*output_list)
