my_f_r = open("text_5_4.txt", "r")
my_f_w = open("text_5_4_result.txt", "a")
i = 0
russian_list = ['Один -', 'Два -', 'Три -', 'Четыре -']
for line in my_f_r:
    current_list = line.split('-')
    current_list.pop(0)
    current_list.insert(0, russian_list[i])
    my_f_w.writelines(current_list)
    i += 1
my_f_r.close()
my_f_w.close()
