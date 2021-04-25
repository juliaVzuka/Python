def division(divid, divis):
    """
    Делит одно число на другое.

    :param divid: делимое, float
    :param divis: делитель, float
    :return: Возвращает результат деления делимого на делитель, округленный до двух знаков после запятой.
    """
    return round(divid / divis, 2)

a = float(input('Введите делимое:'))
b = 0
while b == 0:
    b = float(input('Введите делитель, отличный от нуля: '))
print(f"Результат деления {a} на {b} равен {division(a, b)}")




