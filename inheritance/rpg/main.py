from warrior import Warrior
from mage import Mage

warrior = Warrior("Kratos")
mage = Mage("Merlin")

print("\nRound 1:")
warrior.attack(mage)
mage.cast_spell(warrior, "Fireball")
print("\nRound 2:")
warrior.charge_attack(mage)
mage.cast_spell(warrior, "Typhoon")
warrior.charge_attack(mage)
print("\n!--- Battles end ---!")
if mage.is_alive():
    print(f"Long live {mage._name}")
else:
    print(f"{mage._name} died prematurely")
