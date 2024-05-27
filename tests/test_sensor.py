import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.Car_Park = CarPark("222 Holland",100)
        self.EntrySensor = EntrySensor(1,CarPark("222 Holland",100),True)

    def test_EntrySensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.EntrySensor,Sensor)
        self.assertEqual(self.EntrySensor.id,1)
        self.assertIsInstance(self.EntrySensor.car_park,CarPark)
        self.assertEqual(self.EntrySensor.is_active, True)

    def test_detect_vehicle(self):
        self.assertIn('FAKE-',self.EntrySensor.detect_vehicle())

"""
class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.CarPark = CarPark("222 Holland", 100)
        self.CarPark.plates = ["FAKE001", "FAKE002", "FAKE003"]
        self.ExitSensor = ExitSensor(2, CarPark("222 Holland", 100), True)

    def test_ExitSensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.ExitSensor, Sensor)
        self.assertEqual(self.ExitSensor.id, 2)
        self.assertIsInstance(self.ExitSensor.car_park, CarPark)
        self.assertEqual(self.ExitSensor.is_active, True)

    def test_detect_vehicle(self):
        self.CarPark.remove_car("FAKE001")
        self.ExitSensor.update_car_park(self.ExitSensor._scan_plate())
        self.ExitSensor.detect_vehicle()
        self.assertEqual(CarPark.plates.contains("FAKE001"), False)

"""