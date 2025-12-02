import unittest
from solution import shift

class MyTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(shift("L", 68, 50), 82)

    def test_2(self):
        self.assertEqual(shift("R", 48, 52), 0)

    def test_3(self):
        self.assertEqual(shift("R", 147, 52), 99)

    def test_4(self):
        self.assertEqual(shift("L", 147, 52), 5)

    def test_5(self):
        self.assertEqual(shift("R", 200, 0), 0)

    def test_6(self):
        self.assertEqual(shift("R", 972, 0), 72)

if __name__ == '__main__':
    unittest.main()