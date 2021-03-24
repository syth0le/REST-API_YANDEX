from enum import Enum


class CourierType(Enum):
    """Enum for getting courier_type"""

    foot = "foot"
    bike = "bike"
    car = 'car'

    def __str__(self):
        return str(self.value)
