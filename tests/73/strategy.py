from limits.limits import *
from hypothesis.strategies import lists, integers

q = lists(integers(min_value=VERY_SMALL_INT_NEGATIVE, max_value=VERY_SMALL_INT), max_size=SMALL_SEQUENCE_LEN)

strategy = q
