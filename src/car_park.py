from sensor import Sensor
from display import Display
class CarPark: ## pascal case good for identifying classes
    def __init__(self,
                 location = "Unknown",
                 capacity = 0,
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  ## this is better
        self.sensors = sensors or []
        self.displays = displays or []

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

