from limits.limits import *
from hypothesis.strategies import integers

n = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = n
