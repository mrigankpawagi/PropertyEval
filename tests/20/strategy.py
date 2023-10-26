import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, floats, integers, one_of

numbers = lists(one_of(floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT), integers(min_value=MIN_INT, max_value=MAX_INT)), min_size=2, max_size=MAX_SEQUENCE_LEN)

strategy = numbers
