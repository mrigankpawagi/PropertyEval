from limits.limits import *
from hypothesis.strategies import integers

decimal = integers(min_value=0, max_value=MAX_INT)

strategy = decimal
