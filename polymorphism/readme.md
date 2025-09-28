### **Exercise 4: Polymorphism Challenge - The Magical Device Registry**

**Quest:** Your hero has a collection of various magical devices that all need to be activated.

**Your Task:**
1.  (Re-use or adapt from previous exercises if helpful, but don't strictly require inheritance for this one, focus on duck typing).
2.  Create at least three different classes for magical devices:
    *   `LightOrb`: Has an `activate()` method that prints "Light Orb glows brightly!"
    *   `SoundAmplifier`: Has an `activate()` method that prints "Sound Amplifier emits a resonant hum!"
    *   `HealingPylon`: Has an `activate()` method that prints "Healing Pylon radiates soothing energy!"
    *   (Optional: Add another unique method to each, like `pulse_light()`, `change_volume()`, `heal_amount()`, to show they are distinct beyond `activate()`).
3.  Create a function `activate_all_devices(device_list)` that takes a list of device objects.
4.  Inside `activate_all_devices`, iterate through the `device_list` and call the `activate()` method on each device. Demonstrate how this works seamlessly for all types of devices without knowing their specific class beforehand.