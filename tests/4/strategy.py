from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, floats

numbers = lists(floats(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = numbers
