import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers, floats, one_of

n = integers(min_value=MIN_INT, max_value=MAX_INT)
x = one_of(integers(), floats())
y = one_of(integers(), floats())

strategy = n, x, y
