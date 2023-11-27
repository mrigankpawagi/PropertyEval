from limits.limits import *
from hypothesis.strategies import lists, integers, floats, one_of

xs = lists(one_of(integers(), floats()), min_size=1, max_size=MAX_SEQUENCE_LEN).filter(lambda x: len(x) % 2 == 0 and x[-1] != 0)

strategy = xs
