class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.', self.title)


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки.', self.title)


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки.', self.title)


class Handler(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки.', self.title)


s1 = Stationary('Кисть.')
s2 = Pen('Ручка.')
s3 = Pencil('Карандаш.')
s4 = Handler('Маркер.')
s1.draw()
s2.draw()
s3.draw()
s4.draw()
