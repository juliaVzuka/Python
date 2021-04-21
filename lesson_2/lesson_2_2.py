my_list = list(input('Введите любой набор символов: '))
print('Исходный список:   ', my_list)
el = 0
while el < len(my_list) - 1:
    my_list[el], my_list[el+1] = my_list[el+1], my_list[el]
    el = el + 2
print('Измененный список: ', my_list)