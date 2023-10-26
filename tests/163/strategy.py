import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers

a = integers(min_value=1, max_value=MAX_INT)
b = integers(min_value=1, max_value=MAX_INT)

strategy = a, b
