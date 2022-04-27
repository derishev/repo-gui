class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Pen', self.title)

class Pencil(Stationery):
    def draw(self):
        print('Pencil', self.title)

class Handle(Stationery):
    def draw(self):
        print('Handle', self.title)

my_pen = Pen('Ручка')
my_pen.draw()

my_pencil = Pencil('Карандаш')
my_pencil.draw()

my_handle = Handle('Маркер')
my_handle.draw()

me_stat = Stationery('Разное')
me_stat.draw()