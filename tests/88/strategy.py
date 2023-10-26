from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers

array = lists(integers(min_value=0, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = array
