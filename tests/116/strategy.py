from limits.limits import *
from hypothesis.strategies import lists, integers

arr = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = arr
