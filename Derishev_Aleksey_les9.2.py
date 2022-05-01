class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, thick):
        full_mass = self._length * self._width * 0.025 * thick
        return full_mass

my_road = Road(5000, 20)
print(f'Вес асфальтобетона = {my_road.mass(5)} т.')