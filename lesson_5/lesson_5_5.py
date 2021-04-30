num_str = input('Введите набор чисел, разделенных пробелами: ')
with open("user_file_5.txt", "w+") as user_file:
    user_file.write(num_str)
    user_file.seek(0)
    content = user_file.read()
summ = 0
num_list = content.split(' ')
for el in num_list:
     summ = summ + int(el)
print(f'Сумма введенных чисел равна: {summ}.')
