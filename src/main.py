from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
import random

car_park = CarPark("Moondalup", 100, "Moondalup.txt")
entry_sensor = EntrySensor(1, CarPark(car_park), True)
exit_sensor = ExitSensor(2, CarPark(car_park), True)
display = Display(1, CarPark(car_park), "Welcome to Moondalup", True)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

for i in range(10):
    entry_sensor.detect_vehicle()

print(car_park.plates)

for i in range(2):
    exit_sensor.detect_vehicle() ## THIS SHOULD WORK I DONT KNOW WHY

car_park.to_json()
print("Car park state saved to config.json")

    # Load car park state from JSON
