from limits.limits import *
from hypothesis.strategies import integers

a = integers(min_value=1, max_value=MAX_INT)
b = integers(min_value=1, max_value=MAX_INT)

strategy = a, b
