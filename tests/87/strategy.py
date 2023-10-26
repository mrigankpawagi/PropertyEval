import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers, lists

lst = lists(lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
x = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = lst, x
