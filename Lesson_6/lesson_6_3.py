class Worker:

    def __init__(self, name, surname, position, incom):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = incom


class Position(Worker):
    def __init__(self, name, surname, position, incom):
        super().__init__(name, surname, position, incom)


    def get_full_name(self):
        print('Полное имя сотрудника: ', self.name, self.surname)

    def get_total_incom(self):
        print('Зарплата сотрудника, включая премию: ', self._incom.get('wage') + self._incom.get('bonus'))


p1 = Position('John', 'Lennon', 'vocals', {'wage': 1000, 'bonus': 200})
p2 = Position('Paul', 'McCartney', 'guitar', {'wage': 1500, 'bonus': 300})

print(p1.position)
p1.get_full_name()
p1.get_total_incom()
print(p2.position)
p2.get_full_name()
p2.get_total_incom()
