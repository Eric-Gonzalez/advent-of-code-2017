from advent.utils import nth

UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)


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


class SpiralMemory(object):
    @staticmethod
    def calc_steps(mem_location):
        (x, y) = nth(generate_spiral(), mem_location - 1)
        return abs(x) + abs(y)
