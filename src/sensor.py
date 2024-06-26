from abc import ABC, abstractmethod  ## decorator, like property,
import random
# automatically did this when implementing abstract method? works either way
class Sensor(ABC):
    def __init__(self,
                 id,
                 car_park,
                 is_active=False
                 ):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0, 999), '03d')

    @abstractmethod  ## everyone inheriting this will need to implement it
    def update_car_park(self, plate):
        pass

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)
        return plate

    def __str__(self):
        return f'Sensor{self.id} : {"is on" if self.is_active else "is off"}'


class EntrySensor(Sensor): ## added checks for the display to show the welcome message and goodbye message
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        self.car_park.update_display(True)
        print(f"Incoming vehicle, Plate:{plate}")


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        self.car_park.update_display(False)
        print(f"Outgoing vehicle, Plate: {plate}")
