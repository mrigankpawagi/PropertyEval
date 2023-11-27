from limits.limits import *
from hypothesis.strategies import builds, integers, shared

def create(x: int, y: int):
    return f"{x} apples and {y} oranges"

def create_n(x: int, y: int, z: int):
    return x + y + z

i = integers(min_value=0, max_value=MAX_INT)
a = shared(i)
b = shared(i)
c = shared(i)

s = builds(create, a, b)
n = builds(create_n, a, b, c)

strategy = s, n
