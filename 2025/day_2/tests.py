import unittest
from solution import check, slice_n_diced, factors, main


class MyTests(unittest.TestCase):
    # # 11-22 still has two invalid IDs, 11 and 22.
    # def example_step_1(self):
    #     self.assertEqual(check("11-22"), 33)
    # # 95-115 now has two invalid IDs, 99 and 111.
    # def example_step_2(self):
    #     self.assertEqual(check("95-115"), 210)

    # # 998–1012 now has two invalid IDs, 999 and 1010.
    # def test_range_998_1012(self):
    #     self.assertEqual(check("998-1012"), 2009)

    # # 1188511880–1188511890 still has one invalid ID, 1188511885.
    # def test_range_1188511880_1188511890(self):
    #     self.assertEqual(check("1188511880-1188511890"), 1188511885)

    # # 222220–222224 still has one invalid ID, 222222.
    # def test_range_222220_222224(self):
    #     self.assertEqual(check("222220-222224"), 222222)

    # # 1698522–1698528 still contains no invalid IDs.
    # def test_range_1698522_1698528(self):
    #     self.assertEqual(check("1698522-1698528"), 0)

    # # 446443–446449 still has one invalid ID, 446446.
    # def test_range_446443_446449(self):
    #     self.assertEqual(check("446443-446449"), 446446)

    # # 38593856–38593862 still has one invalid ID, 38593859.
    # def test_range_38593856_38593862(self):
    #     self.assertEqual(check("38593856-38593862"), 38593859)

    # # 565653–565659 now has one invalid ID, 565656.
    # def test_range_565653_565659(self):
    #     self.assertEqual(check("565653-565659"), 565656)

    # # 824824821–824824827 now has one invalid ID, 824824824.
    # def test_range_824824821_824824827(self):
    #     self.assertEqual(check("824824821-824824827"), 824824824)

    # # 2121212118–2121212124 now has one invalid ID, 2121212121.
    # def test_range_2121212118_2121212124(self):
    #     self.assertEqual(check("2121212118-2121212124"), 2121212121)

    # def test_range_462_664(self):
    #     self.assertEqual(check("462-664"), 555)

    # def test_slicer_true(self):
    #     self.assertEqual(slice_n_diced("565656"), True)

    # def test_slicer_false(self):
    #     self.assertEqual(slice_n_diced("565653"), False)

    # def test_slicer_fail(self):
    #     self.assertEqual(slice_n_diced("824824824"), True)

    # def test_factors(self):
    #     self.assertEqual(factors(4), {2})

    def test_main(self):
        self.assertEqual(main(), 54446379122)

if __name__ == "__main__":
    unittest.main()