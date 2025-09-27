from magical_vehicle import MagicalVehicle


class User:
    def __init__(self, name):
        self.name = name

    def travel_by(self, vehicle: MagicalVehicle):
        print(f"user {self.name} traveled by {vehicle.get_name()}")
