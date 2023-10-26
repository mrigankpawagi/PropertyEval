import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers

num = integers(min_value=0, max_value=1000)
need = integers(min_value=0, max_value=1000)
remaining = integers(min_value=0, max_value=1000)

strategy = num, need, remaining
