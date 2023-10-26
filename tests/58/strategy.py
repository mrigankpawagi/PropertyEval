from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers

l1 = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)
l2 = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = l1, l2
