from limits.limits import *
from hypothesis.strategies import integers

n = integers(min_value=2, max_value=MAX_INT)

strategy = n
