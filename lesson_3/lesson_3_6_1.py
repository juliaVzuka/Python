def int_func(user_string):
    """
    Заменяет первую букву строки на заглавную

    :param user_string: строка, str
    :return: Возвращает строку с первой звглавной буквой
    """
    return user_string.capitalize()


result_list = []
user_string = input('Ведите строку из слов, разделенных пробелом: ')
user_list = user_string.split(' ')
for i in range(len(user_list)):
    result_list.insert(i, int_func(user_list[i]))
print(' '.join(result_list))

