### **Exercise 1: Encapsulation Challenge - The Secure Chest**

**Quest:** Your hero has found a magical chest! It has a `lock_status` (boolean: True for locked, False for unlocked) and `contents` (a list of items). The chest can only be opened (`unlock()`) and closed (`lock()`) with a specific `key_code`. If the chest is unlocked, you can `add_item()` or `remove_item()`.

**Your Task:**
1.  Create a `MagicChest` class.
2.  Encapsulate the `lock_status` and `contents` so they cannot be directly modified from outside the class.
3.  Implement `__init__`, `unlock(key_code)`, `lock(key_code)`, `add_item(item)`, and `remove_item(item)`.
4.  Ensure `add_item` and `remove_item` only work if the chest is unlocked.
5.  Provide a public method `get_contents()` to view the items.