from limits.limits import *
from hypothesis.strategies import lists, integers

lst = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = lst
