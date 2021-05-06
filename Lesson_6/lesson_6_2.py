class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asph_mass(self):
        thickness = 5
        mass_per_unit = 25
        return print(
            f'Для строительства понадобится {self._length * self._width * thickness * mass_per_unit} кг асфальта')


road_length = float(input('Введите длинну дороги(м) : '))
road_width = float(input('Введите ширину дороги(м) : '))
a1 = Road(road_length, road_width)
a1.asph_mass()
