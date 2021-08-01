class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('{} запуск отрисовки'.format(self.title))


class Pen(Stationery):
    def draw(self):
        print('{} РУЧКА запуск отрисовки'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('{} КАРАНДАШ запуск отрисовки'.format(self.title))


class Handle(Stationery):
    def draw(self):
        print('{} МАРКЕР запуск отрисовки'.format(self.title))

    stationery = Stationery('Кисть')
    pen = Pen('ручка синяя')
    pencil = Pencil('карандаш черный')
    handle = Handle('маркер желтый')
    stationery.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
