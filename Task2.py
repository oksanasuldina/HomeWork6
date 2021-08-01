class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self, mass_asphalt, thickness):
        return (self._length * self._width * mass_asphalt * thickness)/1000


r = Road(20, 5000)
print(r.mass_asphalt(25, 5))
