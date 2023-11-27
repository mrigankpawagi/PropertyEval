from limits.limits import *
from hypothesis.strategies import lists, integers

lst = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = lst
