import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers, floats, one_of

l = lists(one_of(integers(), floats()), max_size=MAX_SEQUENCE_LEN)

strategy = l
