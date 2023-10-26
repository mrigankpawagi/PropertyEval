import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers

lst = lists(integers(min_value=1, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = lst
