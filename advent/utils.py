def mapt(fn, *args):
    """Do a map, and make the results into a tuple."""
    return tuple(map(fn, *args))


def first(iterable, default=None):
    "The first item in an iterable, or default if it is empty."
    return next(iter(iterable), default)
