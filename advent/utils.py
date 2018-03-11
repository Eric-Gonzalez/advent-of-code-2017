def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))
