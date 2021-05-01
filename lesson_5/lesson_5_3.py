my_f = open("text_5_3.txt", "r")
summ = 0
i = 0
print('Меньше 20 тыс. зарабатывают:', )
for line in my_f:
    i += 1
    current_string = line
    current_list = line.split(' ')
    summ = summ + int(current_list[1])
    if int(current_list[1]) < 20:
        print(f'{current_list[0]}')
print(f'\nСредняя заработная плата равна {summ/i} тыс.')
my_f.close()
