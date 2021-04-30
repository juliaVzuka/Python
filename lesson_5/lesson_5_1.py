user_string_list = []
i = 0
user_string = ''
while user_string != '\n':
    i += 1
    user_string = input('Введите строку для записи в файл или пустую строку для прекращения работы: ')
    user_string = user_string + '\n'
    user_string_list.append(user_string)
user_file = open("user_file.txt", "w")
user_file.writelines(user_string_list)
user_file.close()
