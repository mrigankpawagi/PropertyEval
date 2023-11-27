from limits.limits import *
from hypothesis.strategies import integers, lists, floats, one_of

lst = lists(one_of(integers(min_value=MIN_INT, max_value=MAX_INT), floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)), max_size=MAX_SEQUENCE_LEN)

strategy = lst
