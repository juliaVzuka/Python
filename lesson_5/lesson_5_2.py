my_f = open("text_5_2.txt", "r")
content = my_f.readlines()
my_f.close()
print(f'В файле {len(content)} строки.')
i = 0
for el in content:
    word_list = el.split(' ')
    i += 1
    print(f'Количество слов в {i}-ой строке: {len(word_list)} ')
