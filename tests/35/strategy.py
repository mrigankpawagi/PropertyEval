from limits.limits import *
# Groundtruth is wrong because CONTRACT does not handle empty lists!

from hypothesis.strategies import lists, integers, floats, one_of

l = lists(one_of(integers(), floats()), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = l
