class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('{} машина поехала'.format(self.name))

    def stop(self):
        print('{} машина остановилась'.format(self.name))

    def turn(self, direction):
        if direction == 0:
            print('{} машина повернула налево'.format(self.name))
        else:
            print('{} машина повернула направо'.format(self.name))

    def show_speed(self):
        print('{} скорость автомобиля {}'.format(self.name, self.speed))


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('{} ПРЕВЫШЕНИЕ СКОРОСТИ! Скорость автомобиля {}'.format(self.name, self.speed))
        else:
            print('{} скорость автомобиля {}'.format(self.name, self.speed))


class SportCar(Car):
    def show_speed(self):
        if self.speed > 150:
            print('{} Скорость автомобиля опасна для жизни {}'.format(self.name, self.speed))
        else:
            print('{} скорость автомобиля {}'.format(self.name, self.speed))


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('{} ПРЕВЫШЕНИЕ СКОРОСТИ! Скорость автомобиля {}'.format(self.name, self.speed))
        else:
            print('{} скорость автомобиля {}'.format(self.name, self.speed))


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    toyota = Car(100, 'Белая', 'Toyota')
    toyota.go()
    toyota.stop()
    toyota.turn(50)
    toyota.show_speed()
    сhevrolet = TownCar(90, 'Красная', 'Chevrolet')
    сhevrolet.go()
    сhevrolet.stop()
    сhevrolet.turn(30)
    сhevrolet.show_speed()





