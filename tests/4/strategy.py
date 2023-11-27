from limits.limits import *
from hypothesis.strategies import lists, floats

numbers = lists(floats(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = numbers
