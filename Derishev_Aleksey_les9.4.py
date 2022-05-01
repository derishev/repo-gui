class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Мы поехали')


    def stop(self):
        print('Я остановился')
        self.speed = 0

    def turn(self, direction):
        if direction == 'left':
            print('Поворачиваем на лево')
        elif direction == 'right':
            print('Поворачиваем направо')
        else:
            print('Я незнаю куда поворачивать')

    def show_speed(self):
        print(f'Моя скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Мы поехали')
        if self.speed > 60:
            print('Мы едем слишком быстро')

class SportCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Мы поехали')
        if self.speed > 40:
            print('Мы едем слишком быстро')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


if __name__ == '__main__':
    police_car = PoliceCar(80, 'blue', 'Ivan')
    police_car.go()
    sport_car = SportCar(90, 'red', 'Petr')
    sport_car.turn('left')
    work_kar = WorkCar(50, 'black', 'Kosty')
    work_kar.go()
    town_car = TownCar(60, 'green', 'Aleks')
    town_car.show_speed()
    town_car.stop()
    town_car.show_speed()