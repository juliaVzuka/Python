def my_func_2(my_string):
    """
    Разделяет введенную строку из чисел и пробелов по пробелам, полученные числа суммирует.

    :param my_string: строка с пробелами, str
    :return: Возвращает сумму чисел из введенной строки.
    """
    result = 0
    my_list = my_string.split(' ')
    for i in range(len(my_list)):
        if my_list[i] == '':
            break
        result = result + int(my_list[i])
    return result


def my_func_1(my_string):
    """
    Проверяет, есть ли во введенной строке спецсимволы. Если есть, то обрезает строку по первому
    встреченному спецсимволу.

    :param my_string: строка из чисел, пробелов и, возможно, спецсимволов.
    :return: Возвращает исходную строку, если в ней не было спецсимволов и обрезанную, если были.
    """
    global flag
    specials = ".,:;!?_*-+=()/#%&$@"
    for char in specials:
        if char in my_string:
            flag = True
            checked_string = my_string[0:my_string.index(char)]
            break
    if not flag:
        return my_string
    else:
        return checked_string


checked_string = ''
overall_summ = 0
temp_summ = 0
flag = False
print('Программа вычисляет сумму чисел, введенных рользователем.')
print('Если среди чисел встретится один из спецсимволов: .,:;!?_*-+=()/#%&$@ , то')
print('программа вычислит сумму чисел до первого введенного спецсимвола и прекратит работу.')
while not flag:
    user_string = input('Введите несколько чисел, разделенных пробелом: ')
    checked_string = my_func_1(user_string)
    temp_summ = my_func_2(checked_string)
    overall_summ = overall_summ + temp_summ
    print("Сумма чисел в последней введенной строке равна: ", temp_summ)
    print("Сумма чисел во всех введенных строках: ", overall_summ)

