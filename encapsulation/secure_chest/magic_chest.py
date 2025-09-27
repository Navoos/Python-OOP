class MagicChest:
    def __init__(self, key_code, lock_status=False, contents=[]):
        self.__key_code = key_code
        self._lock_status = lock_status
        self.__contents = contents

    def lock(self, key_code):
        if self.__key_code == key_code:
            self._lock_status = True
            print("Chest locked")
        else:
            print("Invalid or wrong key code.")

    def unlock(self, key_code):
        if self.__key_code == key_code:
            self._lock_status = False
            print("Chest unlocked")
        else:
            print("Invalid or wrong key code.")

    def add_item(self, item):
        if not self._lock_status:
            self.__contents.append(item)
            print(f"Item {item} added to the chest")
        else:
            print("Chest is locked. Cannot add item.")

    def remove_item(self, item):
        if not self._lock_status and item in self.__contents:
            self.__contents.remove(item)
            print(f"Item {item} removed from the chest")
        else:
            print("Chest is locked or item does not exist. Cannot remove item.")

    def get_lock_status(self):
        return self._lock_status


if __name__ == "__main__":
    my_chest = MagicChest("1234", lock_status=True)
    my_chest.add_item("Olive oil")
    my_chest.unlock("1234")
    my_chest.add_item("Bat")
    my_chest.remove_item("Olive oil")
    my_chest.lock("1234")
    print(f"Chest lock status: {my_chest.get_lock_status()}")
