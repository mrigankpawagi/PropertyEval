import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN, VERY_SMALL_INT, VERY_SMALL_INT_NEGATIVE, SMALL_SEQUENCE_LEN
from hypothesis.strategies import lists, integers

q = lists(integers(min_value=VERY_SMALL_INT_NEGATIVE, max_value=VERY_SMALL_INT), max_size=SMALL_SEQUENCE_LEN)
w = integers(min_value=-VERY_SMALL_INT, max_value=VERY_SMALL_INT * 2)

strategy = q, w
