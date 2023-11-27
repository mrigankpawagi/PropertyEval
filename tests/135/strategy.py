from limits.limits import *
from hypothesis.strategies import lists, integers, floats, one_of

lst = lists(one_of(integers(), floats()), max_size=MAX_SEQUENCE_LEN, unique=True)

strategy = lst
