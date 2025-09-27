from abc import ABC, abstractmethod


class MagicalVehicle(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def travel(self, destination: str) -> str:
        pass

    @abstractmethod
    def get_speed(self) -> str:
        pass

    def get_name(self):
        return self._name
