from collections import defaultdict

from advent.utils import nth, first

UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)


def neighbors(point):
    x, y = point
    return ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))


def generate_spiral():
    """
    Heavily based on Peter Norvig's approach
    :return:
    """
    x = y = s = 0
    yield (x, y)
    while True:
        for (dx, dy) in (RIGHT, UP, LEFT, DOWN):
            if dy:
                s += 1
            for _ in range(s):
                x += dx
                y += dy
                yield (x, y)


def generate_spiral_sum():
    grid_values = defaultdict(int)
    for i in generate_spiral():
        grid_values[i] = sum(grid_values[a] for a in neighbors(i)) or 1
        yield grid_values[i]


class SpiralMemory(object):
    @staticmethod
    def calc_steps(mem_location):
        (x, y) = nth(generate_spiral(), mem_location - 1)
        return abs(x) + abs(y)

    @staticmethod
    def calc_sum_of_adjacent_squares(memory_location):
        return first(x for x in generate_spiral_sum() if x > memory_location - 1)
