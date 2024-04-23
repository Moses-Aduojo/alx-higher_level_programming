import unittest
from models.base import Base  # Import the Base class from your module

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        # Test initialization with provided id
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_init_without_id(self):
        # Test initialization without provided id
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)  # First object should have id = 1
        self.assertEqual(obj2.id, 2)  # Second object should have id = 2

if __name__ == '__main__':
    unittest.main()
