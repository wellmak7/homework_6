class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.m = 25
        self.f = 5

    def calculation(self):
        result = self._length * self._width * self.m * self.f
        print(result)

trying = Road(1, 2)
trying.calculation()

