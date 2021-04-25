def int_func(user_string):
    """
    Заменяет первую букву строки на заглавную

    :param user_string: строка, str
    :return: Возвращает строку с первой звглавной буквой
    """
    return user_string.capitalize()


my_string = input('Ведите слово из маленьких латинских букв: ')
print(int_func(my_string))
