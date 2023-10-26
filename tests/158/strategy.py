import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text, lists

words = lists(text(alphabet='abc', max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = words
