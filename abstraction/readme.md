### **Exercise 2: Abstraction Challenge - The Magical Transportation Network**

**Quest:** Your hero needs to travel across the land using different modes of magical transportation. You need to create an abstract transportation system.

**Your Task:**
1.  Define an abstract base class `MagicalVehicle` using the `abc` module.
2.  `MagicalVehicle` should have an `__init__` that takes a `name` and sets it.
3.  It must define *abstract methods*:
    *   `travel(destination)`: Prints how the vehicle travels to the destination.
    *   `get_speed()`: Returns the average speed of the vehicle.
4.  Create two concrete subclasses:
    *   `FlyingCarpet`: `travel`s by "soaring through the skies", `get_speed` returns 50 km/h.
    *   `TeleportationDevice`: `travel`s by "instantly shimmering to", `get_speed` returns "instant" (handle this appropriately, maybe a very high number or a special string).
5.  Demonstrate how you can use both `FlyingCarpet` and `TeleportationDevice` objects interchangeably through the `MagicalVehicle` abstraction.