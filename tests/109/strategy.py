from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers

arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), unique=True, max_size=MAX_SEQUENCE_LEN)

strategy = arr
