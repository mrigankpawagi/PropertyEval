from limits.limits import *
from hypothesis.strategies import lists, integers

arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = arr
