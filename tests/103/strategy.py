from limits.limits import *
from hypothesis.strategies import integers

n = integers(min_value=1, max_value=MAX_INT)
m = integers(min_value=1, max_value=MAX_INT)

strategy = n, m
