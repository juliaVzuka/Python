final_dict = {}
with open("text_5_6.txt", "r") as user_file:
    for line in user_file:
        line_content_list = line.split(' ')
        summ = 0
        for el in line_content_list[1:4]:
            if el != '-':
                summ = summ + int(el[0:2])
        final_dict.update({line_content_list[0]: summ})
print(final_dict)
