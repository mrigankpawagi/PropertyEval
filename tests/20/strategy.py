from limits.limits import *
from hypothesis.strategies import lists, floats, integers, one_of

numbers = lists(one_of(floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT), integers(min_value=MIN_INT, max_value=MAX_INT)), min_size=2, max_size=MAX_SEQUENCE_LEN)

strategy = numbers
