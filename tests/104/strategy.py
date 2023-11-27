from limits.limits import *
from hypothesis.strategies import lists, integers

x = lists(integers(min_value=1, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = x
