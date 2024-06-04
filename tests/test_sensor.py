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
