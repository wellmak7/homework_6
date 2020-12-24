class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} едет')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: ', self.speed)

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Вы превысили скорость")

class SportCar(Car):

    pass

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Вы превысили скорость")

class PoliceCar(Car):
    pass

town_car_example = TownCar(100, "Белая", "Ласточка", False)
town_car_example.show_speed()
town_car_example.turn('налево')

sport_car_example = SportCar(200, "Красная", "Мустанг", False)
work_car_example = WorkCar(50, "Коричневая", "Работяга", False)
police_car_example = PoliceCar(500, "Голубая", "Мент", True)

sport_car_example.show_speed()
sport_car_example.turn('направо')

work_car_example.show_speed()
work_car_example.turn('налево')

police_car_example.show_speed()
police_car_example.turn('направо')