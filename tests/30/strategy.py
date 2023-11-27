from limits.limits import *
from hypothesis.strategies import lists, integers

numbers = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = numbers
