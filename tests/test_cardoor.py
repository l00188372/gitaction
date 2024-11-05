import unittest
from car_doors import CarDoorsClass 

class TestCarDoorsClass(unittest.TestCase):
    
    def setUp(self):
        """Setup for each test method. This is run before each test."""
        self.car = CarDoorsClass()

    def test_initial_doors(self):
        """Test that the initial number of doors is 0."""
        self.assertEqual(self.car.get_number_of_doors(), 0)

    def test_set_valid_number_of_doors(self):
        """Test setting a valid number of doors."""
        self.car.set_number_of_doors(4)
        self.assertEqual(self.car.get_number_of_doors(), 4)

    def test_set_invalid_number_of_doors(self):
        """Test setting an invalid number of doors (negative value)."""
        with self.assertRaises(ValueError):
            self.car.set_number_of_doors(-1)

    def test_set_invalid_type(self):
        """Test setting a non-integer value for number of doors."""
        with self.assertRaises(ValueError):
            self.car.set_number_of_doors("four")

    def test_set_zero_doors(self):
        """Test setting zero doors (invalid)."""
        with self.assertRaises(ValueError):
            self.car.set_number_of_doors(0)

if __name__ == '__main__':
    unittest.main()
