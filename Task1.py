from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        while True:
            self.__color = 'красный'
            print("\033[31m {}" .format(self.__color))
            sleep(7)
            self.__color = 'желтый'
            print("\033[33m {}" .format(self.__color))
            sleep(2)
            self.__color = 'зеленый'
            print("\033[32m {}" .format(self.__color))
            sleep(10)
            self.__color = 'желтый'
            print("\033[33m {}" .format(self.__color))
            sleep(2)


traffic_lights = TrafficLight()
traffic_lights.running()


