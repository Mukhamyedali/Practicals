import random
from car import Car


class UnreliableCar(Car):
    """Car that sometimes doesn't drive depending on reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive if random chance allows."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
