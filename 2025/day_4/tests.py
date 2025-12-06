import unittest
from solution import main


class MyTests(unittest.TestCase):        

    def test_main(self):
        self.assertEqual(main(), 43)

if __name__ == "__main__":
    unittest.main()