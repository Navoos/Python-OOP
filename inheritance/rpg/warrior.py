from character import Character


class Warrior(Character):
    def __init__(self, name, health=150, attack_power=20):
        super().__init__(name, health, attack_power)

    def charge_attack(self, other: Character):
        double_damage = self._attack_power * 2
        if other.take_damage(double_damage):
            print(
                f"A swift attack for complete annihilation taking {other._name} head on"
            )
        else:
            print(
                f"I {self._name} thought you were my match, guess the search continues"
            )
