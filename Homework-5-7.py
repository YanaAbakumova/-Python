import json
my_dict = {}
sum_revenue = 0
firms = 0
with open('text_7.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        tmp_list = line.split()
        if float(tmp_list[2]) - float(tmp_list[3]) >= 0:
            sum_revenue += float(tmp_list[2]) - float(tmp_list[3])
            firms += 1
        my_dict.update({tmp_list[0]: round(float(tmp_list[2]) - float(tmp_list[3]), 2)})
    full_list = [my_dict, {'average_profit': round(sum_revenue / firms, 2)}]
    with open('seventh_out_file.json', 'w', encoding='utf-8') as out_file:
        json.dump(full_list, out_file, indent=4, ensure_ascii=False)
