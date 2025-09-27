from light_orb import LightOrb
from sound_amplifier import SoundAmplifier
from healing_pylon import HealingPylon


if __name__ == "__main__":

    def activate_all_devices(device_list):
        for device in device_list:
            device.activate()
            if isinstance(device, LightOrb):
                device.pulse_light()
            elif isinstance(device, SoundAmplifier):
                device.change_volume()
            elif isinstance(device, HealingPylon):
                device.heal_amount(10)

    activate_all_devices([HealingPylon(), LightOrb(), SoundAmplifier()])
