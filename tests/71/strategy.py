import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import floats, integers, one_of

a = one_of(integers(min_value=1), floats(min_value=0, exclude_min=True))
b = one_of(integers(min_value=1), floats(min_value=0, exclude_min=True))
c = one_of(integers(min_value=1), floats(min_value=0, exclude_min=True))

strategy = a, b, c
