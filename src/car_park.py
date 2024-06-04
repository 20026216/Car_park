from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import random
import json
class CarPark:   ## pascal case good for identifying classes
    def __init__(self,
                 location = "Unknown",
                 capacity = 0,
                 log_file ='log.txt',
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  ## this is better
        self.sensors = sensors or []
        self.displays = displays or []

        self.log_file = Path(log_file) ## use this as using file path as strings can get messy eg backslash/frontslash
        if not self.log_file.exists():
            self.log_file.touch()  ## makes log file if it doesn't exist

    def to_json(self):
        with open("config.json", 'w') as file:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, file)
    @staticmethod ## same method regardless of the instance
    def from_json(filename): ## does NOT take an instance, self is removed
        """Allows the creation of an instance of a car park in json.
        >>> car_park = CarPark.from_json('some_file.txt')"""
        with open(filename, 'r') as file:
            conf = json.load(file)
            return CarPark(location=conf["location"],
                           capacity=int(conf["capacity"]),
                           log_file=conf["log_file"])

    def _log_car(self, action, plate):
        with self.log_file.open(mode="a") as file:  ## Opening with pathlib
            file.write(f'{plate} {action} on the {datetime.now().strftime("%d-%m %H:%M")}\n')


    @property      ## makes this behave as an attribute
    def available_bays(self):  ## changed from get_available_bays, for testing
        return max(0, self.capacity - len(self.plates))  # changed so it doesn't return negatives when overfilling the car park
    def __str__(self):         ## makes it better to represent the instance
        return f"Car Park location = {self.location} capacity = {self.capacity}. "


  #  def register_sensor(self, sensor):  ## this sensor is an object, not a class
   #     self.sensors.append(sensor)  ## This code repeats itself

    #def register(self, component):          ## try writing backwards PUT THE EXCEPTIONS FIRST
    #    if isinstance(component, Sensor):   ## writen on the next part
    #        self.sensors.append(component)
    #    elif isinstance(component, Display):
    #        self.displays.append(component)
    #    else:
    #        raise TypeError("Invalid component type!!!")
    def register(self, component): ## better written with exeptions first
        if not isinstance(component, (Sensor, Display)):
            raise TypeError(f"Invalid component type!!!")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)



    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()
        self._log_car('entered', plate)

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()
        self._log_car('exited', plate)

    def update_display(self):
        for display in self.displays:
            display.update({"Bays" : self.available_bays,
            "Temperature": 42})
            print(f"Updating: {display}")
