from limits.limits import *
from hypothesis.strategies import one_of, lists, integers, floats, text

values = lists(one_of(integers(), floats(), text()), min_size=2, max_size=MAX_SEQUENCE_LEN)

strategy = values
