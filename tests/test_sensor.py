import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.Car_Park = CarPark("222 Holland",100)
        self.EntrySensor = EntrySensor(1,self.Car_Park,True)
        self.ExitSensor = ExitSensor(2,self.Car_Park, True)

    def test_EntrySensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.EntrySensor,Sensor)
        self.assertEqual(self.EntrySensor.id,1)
        self.assertIsInstance(self.EntrySensor.car_park,CarPark)
        self.assertEqual(self.EntrySensor.is_active, True)

    def test_detect_vehicle(self):
        self.assertIn('FAKE-',self.EntrySensor.detect_vehicle())

    def test_ExitSensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.ExitSensor,Sensor)
        self.assertEqual(self.ExitSensor.id, 2)
        self.assertIsInstance(self.ExitSensor.car_park,CarPark)
        self.assertEqual(self.ExitSensor.is_active, True)

    def test_exit_sensor_detect_vehicle(self): ## added check for in going and out going vehicles.
        self.EntrySensor.detect_vehicle()
        self.assertIn('FAKE-',self.ExitSensor.detect_vehicle())