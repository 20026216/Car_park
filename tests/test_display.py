import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(1,CarPark("321 belmont",100),"Welcome to the car park", True)
        self.car_park = CarPark("123 Belmont",100)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")