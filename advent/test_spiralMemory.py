from unittest import TestCase

from advent.spiral_memory import SpiralMemory


class TestSpiralMemory(TestCase):
    def test_calc_steps_1(self):
        self.assertEqual(SpiralMemory.calc_steps(1), 0)

    def test_calc_steps_2(self):
        self.assertEqual(SpiralMemory.calc_steps(12), 3)

    def test_calc_steps_3(self):
        self.assertEqual(SpiralMemory.calc_steps(23), 2)

    def test_calc_steps_4(self):
        self.assertEqual(SpiralMemory.calc_steps(1024), 31)

    def test_calc_steps_5(self):
        self.assertEqual(SpiralMemory.calc_steps(277678), 475)

    def test_calc_sum_of_adjacent_squares_1(self):
        self.assertEqual(SpiralMemory.calc_sum_of_adjacent_squares(1), 1)

    def test_calc_sum_of_adjacent_squares_2(self):
        self.assertEqual(SpiralMemory.calc_sum_of_adjacent_squares(2), 2)

    def test_calc_sum_of_adjacent_squares_3(self):
        self.assertEqual(SpiralMemory.calc_sum_of_adjacent_squares(3), 4)

    def test_calc_sum_of_adjacent_squares_4(self):
        self.assertEqual(SpiralMemory.calc_sum_of_adjacent_squares(4), 4)

    def test_calc_sum_of_adjacent_squares_5(self):
        self.assertEqual(SpiralMemory.calc_sum_of_adjacent_squares(5), 5)

    def test_calc_sum_of_adjacent_squares_6(self):
        self.assertEqual(SpiralMemory.calc_sum_of_adjacent_squares(277678), 279138)
