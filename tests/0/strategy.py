from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import one_of, lists, integers, floats

numbers = lists(one_of(integers(), floats()), max_size=MAX_SEQUENCE_LEN)
threshold = floats(min_value=0.0, exclude_min=True)

strategy = numbers, threshold
