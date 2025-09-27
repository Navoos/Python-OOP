class Character:
    def __init__(self, name, health=100, attack_power=10):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    def take_damage(self, damage) -> bool:
        self._health -= damage
        if self.is_alive():
            print(f"I {self._name} have been hit! Current health: {self._health}")
            return True
        else:
            print(f"I {self._name} can't take anymore damage (gracefully dies)")
            return False

    def attack(self, other):
        if self.is_alive():
            other.take_damage(self._attack_power)
            print(f"I {self._name} have attacked {other._name}!")
        else:
            print(f"I {self._name} can't attack.")

    def is_alive(self) -> bool:
        if self._health > 0:
            return True
        else:
            return False
