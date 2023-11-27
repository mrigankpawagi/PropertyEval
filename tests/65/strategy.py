from limits.limits import *
from hypothesis.strategies import integers

x = integers(min_value=0, max_value=VERY_LARGE_INT)
shift = integers(min_value=0, max_value=MAX_INT)

strategy = x, shift
