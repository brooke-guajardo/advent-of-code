import unittest
from solution import main, bank


class MyTests(unittest.TestCase):

    def test_bank_example_1(self):
        self.assertEqual(bank("987654321111111"), 987654321111)

    def test_bank_example_2(self):
        self.assertEqual(bank("811111111111119"), 811111111119)

    def test_bank_example_3(self):
        self.assertEqual(bank("234234234234278"), 434234234278)

    def test_bank_example_4(self):
        self.assertEqual(bank("818181911112111"), 888911112111)        

    # def test_main(self):
    #     self.assertEqual(main(), "foobar")

if __name__ == "__main__":
    unittest.main()