from limits.limits import *
from hypothesis.strategies import integers, builds

def frac(a, b):
    return f"{a}/{b}"

x = builds(frac, integers(min_value=1, max_value=MAX_INT), integers(min_value=1, max_value=MAX_INT))
n = builds(frac, integers(min_value=1, max_value=MAX_INT), integers(min_value=1, max_value=MAX_INT))

strategy = x, n
