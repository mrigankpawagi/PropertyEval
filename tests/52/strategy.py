from limits.limits import *
from hypothesis.strategies import lists, integers, floats, booleans, one_of

l = lists(one_of(integers(), floats(), booleans()), max_size=MAX_SEQUENCE_LEN)
t = integers()

strategy = l, t
