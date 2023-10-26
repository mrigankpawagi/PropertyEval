from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import one_of, lists, integers, floats, text

values = lists(one_of(integers(), floats(), text()), min_size=2, max_size=MAX_SEQUENCE_LEN)

strategy = values
