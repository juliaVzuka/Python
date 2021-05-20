class MyError(Exception):

    def __init__(self, text):
        self.text = text


num = 0
num_list = []
while num != 'stop':
    num = input(f"Введите число, которое хотите занести список. Для преращения ввода наберите 'stop': ")
    try:
        if not num.isdigit():
            raise MyError("Вы ввели не число, это не будет добавлено в список.")
    except MyError as err:
        print(err)
    else:
        num_list.append(int(num))
print(f"Список введенных чисел: \n{num_list}")
