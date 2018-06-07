from unittest import TestCase

from advent.memory_reallocation import MemoryReallocation


class TestMemoryReallocation(TestCase):

    def test_reallocate(self):
        input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"
        memory_reallocation = MemoryReallocation()
        self.assertEqual(memory_reallocation.reallocate(input), 14029)
