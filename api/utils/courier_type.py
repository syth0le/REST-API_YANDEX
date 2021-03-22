from enum import Enum


class CourierType(Enum):
    foot = "foot"
    bike = "bike"
    car = 'car'

    def __str__(self):
        return str(self.value)
