def my_func(num1, num2, num3):
    """
    Вычисляет сумму двух наибольших из трех введенных чисел.

    :param num1: первое число, int
    :param num2: второе число, int
    :param num3: третье число, int
    :return: Возвращает сумму двух наибольших из трех введенных чисел
    """
    if num1 >= num3 and num2 >= num3:
        return num1 + num2
    elif num1 >= num2 and num3 >= num2:
        return num1 + num3
    else:
        return num2 + num3


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print("Сумма двух наибольших из введенных вами чисел равна: ", my_func(a, b, c))
