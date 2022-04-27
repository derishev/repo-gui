import time
class TrafficLight:
    def __init__(self, color):
        self.__color = color


    def running(self):
        while True:
            if self.__color == 'red':
                print("\033[31m СТОП")
                time.sleep(7)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                print("\033[33m ПРИГОТОВИТСЯ")
                time.sleep(3)
                self.__color = 'green'
            elif self.__color == 'green':
                print("\033[32m ПОЕХАЛИ")
                time.sleep(7)
                break

my_color = TrafficLight('red')
my_color.running()