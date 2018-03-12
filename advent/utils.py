from itertools import islice


def atom(token):
    "Parse a str token into a number, or leave it as a str."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


def vector(line):
    "Parse a str into a tuple of atoms (numbers or str tokens)."
    return mapt(atom, line.replace(',', ' ').split())


def array(lines):
    "Parse an iterable of str lines into a 2-D array. If `lines` is a str, splitlines."
    if isinstance(lines, str): lines = lines.splitlines()
    return mapt(vector, lines)


def mapt(fn, *args):
    """Do a map, and make the results into a tuple."""
    return tuple(map(fn, *args))


def first(iterable, default=None):
    "The first item in an iterable, or default if it is empty."
    return next(iter(iterable), default)


def nth(iterable, position):
    return next(islice(iterable, position, None), None)
