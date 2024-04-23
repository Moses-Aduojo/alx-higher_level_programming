import unittest
from models.rectangle import Rectangle

#unittest for Rectangle class

class TestRectangle(unittest.TestCase):
    def test_init_with_args(self):
        r = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

if __name__ == '__main__':
    unittest.main()
