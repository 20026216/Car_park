from abc import ABC, abstractmethod  ## decorator, like property,
import random
class Sensor(ABC):
    def __init__(self,
                 id,
                 car_park,
                 is_active = False
                 ):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def _scan_plate(self):
        return "FAKE" + format(random.randint(0,999), '03d')
    @abstractmethod  ## everyone inheriting this will need to implement it
    def update_car_park(self, plate):
        pass

    def __str__(self):
        return f'Sensor{self.id} : {"is on" if self.is_active else "is off"}'

class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...