class Date:

    # Зачем нужен конструктор? Mы не создаем экземпляров класса.
    def __init__(self, param):
        self.param = param

    @classmethod
    def date_convert(cls, _date_string):
        date_list = _date_string.split('-')
        date_list_num = []
        for i in range(3):
            date_list_num.append(int(date_list[i]))
        return date_list_num

    @staticmethod
    def date_check(param):
        if param[0] < 1 or param[0] > 31 or param[1] < 1 or param[1] > 12 or param[3] < 1:
            print("Вы ввели некорректную дату!")


date_string = input(f"Ведите дату в формате ДД-ММ-ГГГГ: ")
Date.date_check(Date.date_convert(date_string))
