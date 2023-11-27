from limits.limits import *
from hypothesis.strategies import integers, builds, booleans, shared

def make(n, i, b, t):
    if b:
        return n ** i
    else:
        return t

num = integers(min_value=MIN_INT, max_value=MAX_INT)
n = shared(num, key='n')
x = builds(make, shared(num, key='n'), integers(min_value=0, max_value=MAX_INT), booleans(), shared(num))

strategy = x, n
