from magical_vehicle import MagicalVehicle


class TeleportationDevice(MagicalVehicle):
    def __init__(self, name):
        super().__init__(name)
        self._speed_description = "instantaneous"

    def travel(self, destination):
        return f"{self._name} (Teleportation Device) is instantly shimmering someone to {destination}"

    def get_speed(self):
        return self._speed_description
