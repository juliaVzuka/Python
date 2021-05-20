class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, trademark, year, price):
        self.trademark = trademark
        self.year = year
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, trademark, year, price, color):
        super().__init__(trademark, year, price)
        self.color = color


class Scaner:
    def __init__(self, trademark, year, price, size):
        super().__init__(trademark, year, price)
        self.size = size


class Xerox:
    def __init__(self, trademark, year, price, output):
        super().__init__(trademark, year, price)
        self.output = output


class WareHouse:
    def __init__(self, param):
        self.param = param

    @staticmethod
    def supply(what):
        for i in range(len(wh_contents)):
            wh_contents[i] += what[i]
        return WareHouse(wh_contents)

    @staticmethod
    def equipment_quantity(where):
        supp_list = []
        for _el in equipment_list:
            flag = False
            while not flag:
                input_data = input(f"Сколько {_el} отправить {where}? ")
                try:
                    input_data = int(input_data)
                    if input_data < 0:
                        raise OwnError("Вы ввели отрицательное число!")
                except ValueError:
                    print("Вы ввели не число!")
                except OwnError as err:
                    print(err)
                else:
                    flag = True
                    supp_list.append(int(input_data))
        return supp_list

    def __str__(self):
        return f"\nНа складе: \nпринтеров: {self.param[0]}, сканеров: {self.param[1]}, ксероксов: {self.param[2]}"


class Department(WareHouse):
    def __init__(self, param, name):
        super().__init__(param)
        self.name = name

    #@staticmethod
    def distribution(self, what, where):
        for i in range(len(wh_contents)):
            wh_contents[i] -= what[i]
            where[i] += what[i]
        return Department(where, self.name)

    def __str__(self):
        return f"\n{self.name}: \nпринтеров: {self.param[0]}, сканеров: {self.param[1]}, ксероксов: {self.param[2]}\n"


acc_contents = [0, 0, 0]
admin_contents = [0, 0, 0]
office_contents = [0, 0, 0]
department_contents = [acc_contents, office_contents, admin_contents]
wh_contents = [0, 0, 0]
i = 0
equipment_list = ['принтеров', 'сканеров', 'ксероксов']
where_to_list = ['со склада в бухгалтерию', 'со склада в офис', 'со склада администраторам']
dep_name_list = ['В бухгалтерии', 'В офисе', 'В администрации']
print(f"Поставляем технику на склад.\n")
wh1 = WareHouse.supply(WareHouse.equipment_quantity('на склад'))
print(f"\n{wh1}")
print(f"\nОтправляем технику со склада по отделам.\n")
for el in where_to_list:
    temp_list = Department.equipment_quantity(el)
    temp_dep = Department(temp_list, dep_name_list[i])
    new = temp_dep.distribution(temp_list, department_contents[i])
    print(WareHouse(wh_contents))
    print(new)
    i += 1
