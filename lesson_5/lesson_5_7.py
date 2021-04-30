import json

profit_dict = {}
profit_summ = 0
i = 0
final_list = []
with open("text_5_7.txt", "r") as user_file:
    for line in user_file:
        line_content_list = line.split(' ')
        profit = int(line_content_list[2]) - int(line_content_list[3])
        if profit >= 0:
            profit_summ = profit_summ + profit
            i += 1
        profit_dict.update({line_content_list[0]: profit})
    final_list.append(profit_dict)
    final_list.append({'average profit': round(profit_summ / i, 2)})
    print(final_list)

with open("final_5_7.json", "w") as write_f:
    json.dump(final_list, write_f)
