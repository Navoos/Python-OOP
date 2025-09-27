from flying_carpet import FlyingCarpet
from teleportation_device import TeleportationDevice
from user import User


my_user = User("Navoos")
my_carpet = FlyingCarpet("Rossa")
my_teleportation_device = TeleportationDevice("Blu")
print(my_carpet.get_speed())
print(my_teleportation_device.get_speed())
my_user.travel_by(my_carpet)
print(my_carpet.travel("Antartica"))
print(my_teleportation_device.travel("Pluto"))
