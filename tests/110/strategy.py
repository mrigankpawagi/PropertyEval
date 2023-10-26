import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, integers

lst1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
lst2 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = lst1, lst2
