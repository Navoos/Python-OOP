### **Exercise 3: Inheritance Challenge - The Fantasy RPG Character System**

**Quest:** Your hero is building a new Fantasy RPG! You need a system for different types of characters.

**Your Task:**
1.  Create a base class `Character`. It should have:
    *   `name` (string)
    *   `health` (integer, default 100)
    *   `attack_power` (integer, default 10)
    *   A method `take_damage(amount)` that reduces health and prints a message.
    *   A method `attack(other_character)` that makes this character attack `other_character`, inflicting its `attack_power` as damage.
    *   A method `is_alive()` that returns `True` if health > 0, `False` otherwise.
2.  Create two subclasses that inherit from `Character`:
    *   `Warrior`:
        *   Initial `health` of 150, `attack_power` of 20.
        *   Has a unique method `charge_attack(other_character)` which deals double its normal `attack_power` damage.
    *   `Mage`:
        *   Initial `health` of 80, `attack_power` of 15.
        *   Has a unique method `cast_spell(other_character, spell_name)` which deals damage based on the `spell_name` (e.g., "Fireball" deals 30 damage, "Ice Shard" deals 20). It should call `other_character.take_damage()`.
3.  Demonstrate a small battle simulation between a `Warrior` and a `Mage`.