from limits.limits import *
from hypothesis.strategies import one_of, lists, integers, floats

numbers = lists(one_of(integers(), floats()), max_size=MAX_SEQUENCE_LEN)
threshold = floats(min_value=0.0, exclude_min=True)

strategy = numbers, threshold
