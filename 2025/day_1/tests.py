import unittest
from solution import shift, shift_slow


class MyTests(unittest.TestCase):

    def checker(self, direction, amount, start, expected_pos, expected_hits):
        expected = (expected_pos, expected_hits)
        fast = shift(direction, amount, start)
        slow = shift_slow(direction, amount, start)

        self.assertEqual(
            fast, expected,
            msg=f"FAST mismatch: {direction}{amount} from {start}. "
                f"Got {fast}, expected {expected}"
        )
        self.assertEqual(
            slow, expected,
            msg=f"SLOW mismatch: {direction}{amount} from {start}. "
                f"Got {slow}, expected {expected}"
        )
        self.assertEqual(
            fast, slow,
            msg=f"FAST/SLOW mismatch: {direction}{amount} from {start}. "
                f"Fast={fast}, Slow={slow}"
        )

    # ======================================================
    #  BASIC LEFT ROTATIONS (no wraps)
    # ======================================================

    def test_L_basic(self):
        self.checker("L", 68, 50, 82, 1)

    def test_L_small_no_hit(self):
        self.checker("L", 5, 0, 95, 0)

    def test_L_small_partial_cross(self):
        self.checker("L", 7, 2, 95, 1)

    def test_L_pointing_just_hits_zero(self):
        self.checker("L", 55, 55, 0, 1)

    def test_L_pointing_lands_on_zero(self):
        self.checker("L", 99, 99, 0, 1)


    # ======================================================
    #  BASIC RIGHT ROTATIONS (no wraps)
    # ======================================================

    def test_R_basic(self):
        self.checker("R", 48, 52, 0, 1)

    def test_R_small_no_hit(self):
        self.checker("R", 14, 0, 14, 0)

    def test_R_small_partial_cross(self):
        self.checker("R", 7, 98, 5, 1)

    def test_R_small_from_zero_no_hit(self):
        self.checker("R", 7, 0, 7, 0)


    # ======================================================
    #  FULL WRAPS (no leftover)
    # ======================================================

    def test_L_full_wrap_twice(self):
        self.checker("L", 200, 50, 50, 2)

    def test_R_full_wrap_once(self):
        self.checker("R", 100, 50, 50, 1)

    def test_R_full_wrap_from_zero(self):
        self.checker("R", 100, 0, 0, 1)

    def test_L_full_wrap_from_zero(self):
        self.checker("L", 100, 0, 0, 1)

    def test_R_large_full_wrap(self):
        self.checker("R", 1000, 50, 50, 10)


    # ======================================================
    #  WRAP + PARTIAL WRAP (combined behaviors)
    # ======================================================

    def test_L_wrap_and_partial(self):
        self.checker("L", 147, 52, 5, 1)

    def test_R_wrap_and_partial(self):
        self.checker("R", 148, 52, 0, 2)

    def test_L_wrap_and_partial_HARD(self):
        self.checker("L", 250, 20, 70, 3)

    def test_R_wrap_and_partial_HARD(self):
        self.checker("R", 250, 90, 40, 3)

    def test_L_wrap_then_partial_lands_zero(self):
        self.checker("L", 101, 1, 0, 2)


    # ======================================================
    #  STARTING AT ZERO (special behaviors)
    # ======================================================

    def test_L_from_zero_small_no_hit(self):
        self.checker("L", 5, 0, 95, 0)

    def test_L_from_zero_small_no_hit_2(self):
        self.checker("L", 7, 0, 93, 0)

    def test_R_from_zero_small_no_hit(self):
        self.checker("R", 7, 0, 7, 0)

    def test_R_from_zero_wrap(self):
        self.checker("R", 200, 0, 0, 2)

    def test_R_from_zero_wrap_plus_leftover(self):
        self.checker("R", 150, 0, 50, 1)

    def test_R_from_zero_wrap_big(self):
        self.checker("R", 972, 0, 72, 9)


    # ======================================================
    #  LEFTOVER MOVEMENT EXACT ZERO HITS
    # ======================================================

    def test_L_leftover_lands_on_zero(self):
        self.checker("L", 99, 99, 0, 1)

    def test_L_leftover_crosses_zero(self):
        self.checker("L", 82, 14, 32, 1)


    # ======================================================
    #  COMPLEX / EDGE CASES
    # ======================================================

    def test_C_corrected_no_leftover_zero_cross(self):
        self.checker("R", 1234, 40, 74, 12)

    def test_fail_case_1(self):
        self.checker("L", 250, 10, 60, 3)

    def test_fail_case_2(self):
        self.checker("R", 250, 90, 40, 3)


if __name__ == "__main__":
    unittest.main()
