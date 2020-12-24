class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой.")

class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом.")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером.")

pen_example = Pen("Ручка")
pencil_example = Pencil("Карандаш")
handle_example = Handle("Маркер")

pen_example.draw()
pencil_example.draw()
handle_example.draw()