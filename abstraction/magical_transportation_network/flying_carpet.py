from magical_vehicle import MagicalVehicle


class FlyingCarpet(MagicalVehicle):
    def __init__(self, name):
        super().__init__(name)
        self._speed = 50  # km/h

    def travel(self, destination):
        return f"{self._name} (Flying carpet) is soaring through the skies to {destination}"

    def get_speed(self):
        return f"{self._speed} km/h"
