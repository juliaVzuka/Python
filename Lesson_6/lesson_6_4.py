class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print(f'Cкорость машины {self.speed} км/ч')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Cкорость машины {self.speed} км/ч')
        if self.speed > 60:
            print('Вы превышаете максимальную разрешенную скорость!')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Cкорость машины {self.speed} км/ч')
        if self.speed > 40:
            print('Вы превышаете максимальную разрешенную скорость!')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = SportCar(300, 'красный', 'Ферарри', True)
car1.turn('налево')
car1.show_speed()
car2 = WorkCar(50, 'желтый', 'CAT', True)
car2.show_speed()
car3 = TownCar(80, 'черный', 'Опель', True)
car3.show_speed()
car4 = PoliceCar(120, 'синий', 'Форд', True)
print(car4.name, car4.color, car4.speed)
