from character import Character


class Mage(Character):
    def __init__(self, name, health=80, attack_power=15):
        # Call the parent constructor to initialize the variables
        super().__init__(name, health, attack_power)

    def cast_spell(self, other: Character, spell_name):
        # Check if the spell is known by the mage
        spell_damage = self._get_spell_damage(spell_name)
        if spell_damage:
            if other.take_damage(spell_damage):
                print(
                    f"I {self._name} have casted {spell_name} on to {other._name}. He didn't see it coming"
                )
            else:
                print("You have been a challenging opponent, you have my respect")
        else:
            print(f"I {self._name} cant't remember the spell {spell_name}. I messed up")

    def _get_spell_damage(self, spell_name):
        spells = ["Fireball", "Ice Shard"]
        spells_damage = [30, 20]

        # Match the spell_name with the appropriate spell damage
        for spell_damage, spell in zip(spells_damage, spells):
            if spell == spell_name:
                return spell_damage
        return None
