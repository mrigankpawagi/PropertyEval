from limits.limits import *
from hypothesis.strategies import lists, integers

array = lists(integers(min_value=0, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = array
