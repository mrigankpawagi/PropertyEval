from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers, floats, one_of

l = lists(one_of(integers(), floats()), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = l
